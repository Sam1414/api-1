# Copyright 2015 The TensorFlow Authors. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ==============================================================================
"""Helpers to manipulate a tensor graph in python.
"""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
import copy
import re

import six

from tensorflow.core.framework import attr_value_pb2
from tensorflow.core.framework import graph_pb2
from tensorflow.core.framework import node_def_pb2
from tensorflow.python.framework import dtypes
from tensorflow.python.framework import ops
from tensorflow.python.framework import tensor_util
from tensorflow.python.platform import tf_logging as logging
from tensorflow.python.util import deprecation
from tensorflow.python.util.tf_export import tf_export

_VARIABLE_OPS = {
    "Assign",
    "AssignAdd",
    "AssignSub",
    "Queue",
    "ScatterAdd",
    "ScatterSub",
    "ScatterUpdate",
    "TruncatedNormal",
    "Variable",
    "VariableV2",
}

_CONTROL_FLOW_OP_NAMES_OR_IDENTITY = [
    "Switch",
    "Enter",
    "Exit",
    "Identity",
    "Merge",
    "NextIteration",
]


def _is_variable_op(op):
  """Returns true if 'op' refers to a Variable node."""
  return op in _VARIABLE_OPS


@deprecation.deprecated(
    date=None,
    instructions="Use `tf.compat.v1.graph_util.must_run_on_cpu`")
@tf_export(v1=["graph_util.must_run_on_cpu"])
def must_run_on_cpu(node, pin_variables_on_cpu=False):
  """Returns True if the given node_def must run on CPU, otherwise False.

  Args:
    node: The node to be assigned to a device. Could be either an ops.Operation
      or NodeDef.
    pin_variables_on_cpu: If True, this function will return False if node_def
      represents a variable-related op.

  Returns:
    True if the given node must run on CPU, otherwise False.
  """

  if isinstance(node, ops.Operation):
    node_def = node.node_def
  else:
    assert isinstance(node, node_def_pb2.NodeDef)
    node_def = node

  # If the op is a variable-related op, should we pin it on CPU?
  if pin_variables_on_cpu and _is_variable_op(node_def.op):
    return True

  # Constant operations producing a string or int32 must run on CPU.
  if node_def.op == "Const":
    # Get the value of the 'dtype' attr
    dtype = node_def.attr["dtype"].type
    if dtype == dtypes.string or dtype == dtypes.int32:
      return True

  if node_def.op in ["DynamicStitch", "ParallelDynamicStitch"]:
    dtype = node_def.attr["T"].type
    if dtype == dtypes.int32:
      # DynamicStitch on GPU only works for int32 values.
      return True

  if node_def.op in ["Cast"]:
    dtype = node_def.attr["SrcT"].type
    if dtype == dtypes.int32:
      # Cast on GPU does not works for int32 values.
      return True
  return False


################################################################################
#
# device functions for use in with g.device(...)
#
################################################################################


def _node_name(n):
  if n.startswith("^"):
    return n[1:]
  else:
    return n.split(":")[0]


def _get_colocated_node_name(colocated_node_name):
  """Decodes colocated node name and returns it without loc:@ prepended."""
  colocated_node_decoded = colocated_node_name.decode("utf-8")
  if colocated_node_decoded.startswith("loc:@"):
    return colocated_node_decoded[5:]
  return colocated_node_decoded


def _extract_graph_summary(graph_def):
  """Extracts useful information from the graph and returns them."""
  name_to_input_name = {}  # Keyed by the dest node name.
  name_to_node = {}  # Keyed by node name.

  # Keeps track of node sequences. It is important to still output the
  # operations in the original order.
  name_to_seq_num = {}  # Keyed by node name.
  seq = 0
  for node in graph_def.node:
    n = _node_name(node.name)
    name_to_node[n] = node
    name_to_input_name[n] = [_node_name(x) for x in node.input]
    # Prevent colocated nodes from being lost.
    if "_class" in node.attr:
      for colocated_node_name in node.attr["_class"].list.s:
        name_to_input_name[n].append(
            _get_colocated_node_name(colocated_node_name))
    name_to_seq_num[n] = seq
    seq += 1
  return name_to_input_name, name_to_node, name_to_seq_num


def _assert_nodes_are_present(name_to_node, nodes):
  """Assert that nodes are present in the graph."""
  for d in nodes:
    assert d in name_to_node, "%s is not in graph" % d


def _bfs_for_reachable_nodes(target_nodes, name_to_input_name):
  """Breadth first search for reachable nodes from target nodes."""
  nodes_to_keep = set()
  # Breadth first search to find all the nodes that we should keep.
  next_to_visit = target_nodes[:]
  while next_to_visit:
    node = next_to_visit[0]
    del next_to_visit[0]
    if node in nodes_to_keep:
      # Already visited this node.
      continue
    nodes_to_keep.add(node)
    if node in name_to_input_name:
      next_to_visit += name_to_input_name[node]
  return nodes_to_keep


@deprecation.deprecated(
    date=None,
    instructions="Use `tf.compat.v1.graph_util.extract_sub_graph`")
@tf_export(v1=["graph_util.extract_sub_graph"])
def extract_sub_graph(graph_def, dest_nodes):
  """Extract the subgraph that can reach any of the nodes in 'dest_nodes'.

  Args:
    graph_def: A graph_pb2.GraphDef proto.
    dest_nodes: A list of strings specifying the destination node names.
  Returns:
    The GraphDef of the sub-graph.

  Raises:
    TypeError: If 'graph_def' is not a graph_pb2.GraphDef proto.
  """

  if not isinstance(graph_def, graph_pb2.GraphDef):
    raise TypeError("graph_def must be a graph_pb2.GraphDef proto.")

  if isinstance(dest_nodes, six.string_types):
    raise TypeError("dest_nodes must be a list.")

  name_to_input_name, name_to_node, name_to_seq_num = _extract_graph_summary(
      graph_def)
  _assert_nodes_are_present(name_to_node, dest_nodes)

  nodes_to_keep = _bfs_for_reachable_nodes(dest_nodes, name_to_input_name)

  nodes_to_keep_list = sorted(
      list(nodes_to_keep), key=lambda n: name_to_seq_num[n])
  # Now construct the output GraphDef
  out = graph_pb2.GraphDef()
  for n in nodes_to_keep_list:
    out.node.extend([copy.deepcopy(name_to_node[n])])
  out.library.CopyFrom(graph_def.library)
  out.versions.CopyFrom(graph_def.versions)

  return out


@deprecation.deprecated(
    date=None,
    instructions="Use `tf.compat.v1.graph_util.tensor_shape_from_node_def_name`"
)
@tf_export(v1=["graph_util.tensor_shape_from_node_def_name"])
def tensor_shape_from_node_def_name(graph, input_name):
  """Convenience function to get a shape from a NodeDef's input string."""
  # To get a tensor, the name must be in the form <input>:<port>, for example
  # 'Mul:0'. The GraphDef input strings don't always have the port specified
  # though, so if there isn't a colon we need to add a default ':0' to the end.
  if ":" not in input_name:
    canonical_name = input_name + ":0"
  else:
    canonical_name = input_name
  tensor = graph.get_tensor_by_name(canonical_name)
  shape = tensor.get_shape()
  return shape


def _update_resource_identities(resource_identities, output_graph_def,
                                variable_names_whitelist,
                                variable_names_blacklist):
  """Updates the type of DT_RESOURCE Identity ops.

  Updates the type of the `resource_identities` to the type of the node that
  feed into it if the node is not an input to any other node. Valid nodes are
  generally colocated nodes.

  Args:
    resource_identities: List of NodeDef protos that are Identity ops with the
      type DT_RESOURCE.
    output_graph_def: GraphDef proto.
    variable_names_whitelist: The set of variable names to convert (by default,
                              all variables are converted).
    variable_names_blacklist: The set of variable names to omit converting
                              to constants.
  """
  # Identify the nodes in the graph and the nodes consuming each node.
  map_name_to_node = {}
  map_name_to_inputs = {}
  for node in output_graph_def.node:
    map_name_to_node[node.name] = node
    for unparsed_input_name in node.input:
      if not unparsed_input_name.startswith("^"):
        parsed_input_name = _node_name(unparsed_input_name)
        if parsed_input_name not in map_name_to_inputs:
          map_name_to_inputs[parsed_input_name] = []
        map_name_to_inputs[parsed_input_name].append(node.name)

  for node in resource_identities:
    # Validate the node is not an input to other nodes.
    if node.name in map_name_to_inputs:
      continue

    # Get the type of the Identity node by tracing back through the nodes until
    # we come to a non-Identity or non-control flow node or the type of the node
    # is not DT_RESOURCE.
    input_node = map_name_to_node[_node_name(node.input[0])]
    while (input_node.op in _CONTROL_FLOW_OP_NAMES_OR_IDENTITY and
           input_node.attr["T"].type == dtypes.resource):
      input_node = map_name_to_node[_node_name(input_node.input[0])]

    # Update the type of the Identity node if an Identity, control flow, or
    # VarHandleOp node with a type that is not DT_RESOURCE is found.
    debugging_message = str.encode(
        "This Identity's type was changed from DT_RESOURCE during graph "
        "freezing.")
    if input_node.attr["T"].type != dtypes.resource:
      if (input_node.op in _CONTROL_FLOW_OP_NAMES_OR_IDENTITY
          and _should_convert(
              input_node.input[0],
              variable_names_whitelist,
              variable_names_blacklist)):
        node.attr["T"].CopyFrom(input_node.attr["T"])
        node.attr["_debugging"].s = debugging_message
      elif (input_node.op == "VarHandleOp"
            and _should_convert(
                input_node.name,
                variable_names_whitelist,
                variable_names_blacklist)):
        node.attr["T"].CopyFrom(input_node.attr["dtype"])
        node.attr["_debugging"].s = debugging_message


def _should_convert(name, whitelist, blacklist):
  return ((whitelist is None or name in whitelist)
          and (blacklist is None or name not in blacklist))


@deprecation.deprecated(
    date=None,
    instructions="Use `tf.compat.v1.graph_util.convert_variables_to_constants`")
@tf_export(v1=["graph_util.convert_variables_to_constants"])
def convert_variables_to_constants(sess,
                                   input_graph_def,
                                   output_node_names,
                                   variable_names_whitelist=None,
                                   variable_names_blacklist=None):
  """Replaces all the variables in a graph with constants of the same values.

  If you have a trained graph containing Variable ops, it can be convenient to
  convert them all to Const ops holding the same values. This makes it possible
  to describe the network fully with a single GraphDef file, and allows the
  removal of a lot of ops related to loading and saving the variables.

  Args:
    sess: Active TensorFlow session containing the variables.
    input_graph_def: GraphDef object holding the network.
    output_node_names: List of name strings for the result nodes of the graph.
    variable_names_whitelist: The set of variable names to convert (by default,
                              all variables are converted).
    variable_names_blacklist: The set of variable names to omit converting
                              to constants.

  Returns:
    GraphDef containing a simplified version of the original.

  Raises:
    RuntimeError: if a DT_RESOURCE op is found whose ancestor Variables are both
      blacklisted AND whitelisted for freezing.
  """

  get_input_name = lambda node, index=0: node.input[index].split(":")[0]

  def create_const_op(node_name, dtype, data, data_shape=None):
    """Creates a Const op."""
    output_node = node_def_pb2.NodeDef()
    output_node.op = "Const"
    output_node.name = node_name
    output_node.attr["dtype"].CopyFrom(dtype)
    output_node.attr["value"].CopyFrom(
        attr_value_pb2.AttrValue(
            tensor=tensor_util.make_tensor_proto(
                data, dtype=dtype.type, shape=data_shape)))
    return output_node

  # This graph only includes the nodes needed to evaluate the output nodes, and
  # removes unneeded nodes like those involved in saving and assignment.
  inference_graph = extract_sub_graph(input_graph_def, output_node_names)

  # Identify the ops in the graph.
  map_name_to_node = {
      node.name: node for node in inference_graph.node
  }

  # Get list of variables.
  variable_names = []
  variable_dict_names = []
  resource_op_types = {}

  for node in inference_graph.node:
    if node.op in ["Variable", "VariableV2", "VarHandleOp"]:
      variable_name = node.name
      if not _should_convert(
          variable_name, variable_names_whitelist, variable_names_blacklist):
        continue
      variable_dict_names.append(variable_name)
      if node.op == "VarHandleOp":
        variable_names.append(variable_name + "/Read/ReadVariableOp:0")
      else:
        variable_names.append(variable_name + ":0")
    elif node.op in ["ReadVariableOp", "ResourceGather", "ResourceGatherNd"]:
      # There can be one or more Identity or control flow ops in between the
      # ReadVariableOp and VarHandleOp. Store the ops with the associated
      # dtypes.
      source_op_names = [get_input_name(node)]
      candidate_resource_op_types = {}
      while (source_op_names and map_name_to_node[source_op_names[0]].op in
             _CONTROL_FLOW_OP_NAMES_OR_IDENTITY):
        source_op_name = source_op_names.pop()
        current_node = map_name_to_node[source_op_name]

        if (source_op_name not in resource_op_types and
            source_op_name not in candidate_resource_op_types):
          candidate_resource_op_types[source_op_name] = node.attr["dtype"]
          source_op_names.append(get_input_name(current_node))

        if current_node == "Merge":
          merge_resource_name = get_input_name(current_node, index=1)
          if (merge_resource_name not in resource_op_types
              and merge_resource_name not in candidate_resource_op_types):
            candidate_resource_op_types[merge_resource_name] = (
                node.attr["dtype"])
            source_op_names.append(
                get_input_name(map_name_to_node[merge_resource_name]))

      should_convert_all = None
      for source_node in source_op_names:
        if map_name_to_node[source_node].op != "VarHandleOp":
          raise ValueError("Cannot find the variable that is an input "
                           "to the ReadVariableOp.")
        should_convert_node = _should_convert(
            source_node, variable_names_whitelist, variable_names_blacklist)
        if should_convert_all is None:
          should_convert_all = should_convert_node
        elif should_convert_all != should_convert_node:
          raise RuntimeError(
              "Found DT_RESOURCE node whose ancestor Variables are both "
              "blacklisted AND whitelisted for freezing.  Originating "
              "descendant node: {}.  Ancestor variables: {}.".format(
                  node.name, source_op_names))
      if should_convert_all in (None, True):
        resource_op_types.update(candidate_resource_op_types)

  # Gets map of variables and the associated data.
  if variable_names:
    returned_variables = sess.run(variable_names)
  else:
    returned_variables = []
  variables_data_map = dict(zip(variable_dict_names, returned_variables))
  logging.info("Froze %d variables.", len(returned_variables))

  def _should_convert_ancestor(node):
    input_node = map_name_to_node[_node_name(node.input[0])]
    while (input_node.op in _CONTROL_FLOW_OP_NAMES_OR_IDENTITY and
           input_node.attr["T"].type == dtypes.resource):
      input_node = map_name_to_node[_node_name(input_node.input[0])]
    return _should_convert(input_node.name,
                           variable_names_whitelist,
                           variable_names_blacklist)

  # Reconstruct the graph with constants in place of variables.
  output_graph_def = graph_pb2.GraphDef()
  how_many_converted = 0
  for input_node in inference_graph.node:
    output_node = node_def_pb2.NodeDef()
    if input_node.name in variables_data_map:
      data = variables_data_map[input_node.name]
      output_node = create_const_op(input_node.name, input_node.attr["dtype"],
                                    data, data.shape)
      how_many_converted += 1
    elif input_node.name in resource_op_types:
      # Converts the type of the ops between the ReadVariableOp and VarHandleOp
      # from RESOURCE_DT to the appropriate type based on the input they are
      # referencing. Do not copy shapes due to incorrect shape info.
      output_node.op = input_node.op
      output_node.name = input_node.name
      for in_node in input_node.input:
        output_node.input.append(in_node)
      for attr_name in input_node.attr:
        if str(attr_name) != "_output_shapes":
          output_node.attr[attr_name].CopyFrom(input_node.attr[attr_name])
      output_node.attr["T"].CopyFrom(resource_op_types[input_node.name])
    elif (input_node.op == "ReadVariableOp"
          and _should_convert_ancestor(input_node)):
      # The first branch converts all VarHandleOps of ResourceVariables to
      # constants, so we need to convert the associated ReadVariableOps to
      # Identity ops.
      output_node.op = "Identity"
      output_node.name = input_node.name
      output_node.input.extend([input_node.input[0]])
      output_node.attr["T"].CopyFrom(input_node.attr["dtype"])
      if "_class" in input_node.attr:
        output_node.attr["_class"].CopyFrom(input_node.attr["_class"])
    elif (input_node.op == "ResourceGather"
          and _should_convert_ancestor(input_node)):
      # The first branch converts all VarHandleOps of ResourceGather to
      # constants, so we need to convert the associated ResourceGather to Gather
      # ops with a Const axis feeding into it.
      if input_node.attr["batch_dims"].i != 0:
        raise ValueError("batch_dims != 0 is not supported by freeze_graph.")
      axis_data = input_node.attr["batch_dims"].i
      axis_node_name = input_node.name + "/axis"
      axis_dtype = input_node.attr["Tindices"]
      output_axis_node = create_const_op(axis_node_name, axis_dtype, axis_data)
      output_graph_def.node.extend([output_axis_node])

      output_node.op = "GatherV2"
      output_node.name = input_node.name
      output_node.input.extend(
          [input_node.input[0], input_node.input[1], axis_node_name])
      output_node.attr["Tparams"].CopyFrom(input_node.attr["dtype"])
      output_node.attr["Tindices"].CopyFrom(input_node.attr["Tindices"])
      output_node.attr["Taxis"].CopyFrom(axis_dtype)
      if "_class" in input_node.attr:
        output_node.attr["_class"].CopyFrom(input_node.attr["_class"])
    elif (input_node.op == "ResourceGatherNd"
          and _should_convert_ancestor(input_node)):
      output_node.op = "GatherNd"
      output_node.name = input_node.name
      output_node.input.extend(
          [input_node.input[0], input_node.input[1]])
      output_node.attr["Tparams"].CopyFrom(input_node.attr["dtype"])
      output_node.attr["Tindices"].CopyFrom(input_node.attr["Tindices"])
      if "_class" in input_node.attr:
        output_node.attr["_class"].CopyFrom(input_node.attr["_class"])
    else:
      output_node.CopyFrom(input_node)
    output_graph_def.node.append(output_node)

  # Update the types of the DT_RESOURCE Identity nodes that do not have an
  # associated ReadVariableOp.
  resource_identities = []
  for node in output_graph_def.node:
    if node.op == "Identity" and node.attr["T"].type == dtypes.resource:
      resource_identities.append(node)
  if resource_identities:
    _update_resource_identities(resource_identities,
                                output_graph_def,
                                variable_names_whitelist,
                                variable_names_blacklist)

  output_graph_def.library.CopyFrom(inference_graph.library)
  logging.info("Converted %d variables to const ops.", how_many_converted)
  return output_graph_def


@deprecation.deprecated(
    date=None,
    instructions="Use `tf.compat.v1.graph_util.remove_training_nodes`")
@tf_export(v1=["graph_util.remove_training_nodes"])
def remove_training_nodes(input_graph, protected_nodes=None):
  """Prunes out nodes that aren't needed for inference.

  There are nodes like Identity and CheckNumerics that are only useful
  during training, and can be removed in graphs that will be used for
  nothing but inference. Here we identify and remove them, returning an
  equivalent graph. To be specific, CheckNumerics nodes are always removed, and
  Identity nodes that aren't involved in control edges are spliced out so that
  their input and outputs are directly connected.

  Args:
    input_graph: Model to analyze and prune.
    protected_nodes: An optional list of names of nodes to be kept
      unconditionally. This is for example useful to preserve Identity output
      nodes.

  Returns:
    A list of nodes with the unnecessary ones removed.
  """
  if not protected_nodes:
    protected_nodes = []

  types_to_remove = {"CheckNumerics": True}

  input_nodes = input_graph.node
  names_to_remove = {}
  for node in input_nodes:
    if node.op in types_to_remove and node.name not in protected_nodes:
      names_to_remove[node.name] = True

  nodes_after_removal = []
  for node in input_nodes:
    if node.name in names_to_remove:
      continue
    new_node = node_def_pb2.NodeDef()
    new_node.CopyFrom(node)
    input_before_removal = node.input
    del new_node.input[:]
    for full_input_name in input_before_removal:
      input_name = re.sub(r"^\^", "", full_input_name)
      if input_name in names_to_remove:
        continue
      new_node.input.append(full_input_name)
    nodes_after_removal.append(new_node)

  types_to_splice = {"Identity": True}
  control_input_names = set()
  node_names_with_control_input = set()
  for node in nodes_after_removal:
    for node_input in node.input:
      if "^" in node_input:
        control_input_names.add(node_input.replace("^", ""))
        node_names_with_control_input.add(node.name)

  names_to_splice = {}
  for node in nodes_after_removal:
    if node.op in types_to_splice and node.name not in protected_nodes:
      # We don't want to remove nodes that have control edge inputs, because
      # they might be involved in subtle dependency issues that removing them
      # will jeopardize.
      if node.name not in node_names_with_control_input:
        names_to_splice[node.name] = node.input[0]

  # We also don't want to remove nodes which are used as control edge inputs.
  names_to_splice = {name: value for name, value in names_to_splice.items()
                     if name not in control_input_names}

  nodes_after_splicing = []
  for node in nodes_after_removal:
    if node.name in names_to_splice:
      continue
    new_node = node_def_pb2.NodeDef()
    new_node.CopyFrom(node)
    input_before_removal = node.input
    del new_node.input[:]
    for full_input_name in input_before_removal:
      input_name = re.sub(r"^\^", "", full_input_name)
      while input_name in names_to_splice:
        full_input_name = names_to_splice[input_name]
        input_name = re.sub(r"^\^", "", full_input_name)
      new_node.input.append(full_input_name)
    nodes_after_splicing.append(new_node)

  output_graph = graph_pb2.GraphDef()
  output_graph.node.extend(nodes_after_splicing)
  return output_graph
