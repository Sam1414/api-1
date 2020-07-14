"""Python wrappers around TensorFlow ops.

This file is MACHINE GENERATED! Do not edit.
Original C++ source file: linalg_ops.cc
"""

import collections

from tensorflow.python import pywrap_tfe as pywrap_tfe
from tensorflow.python.eager import context as _context
from tensorflow.python.eager import core as _core
from tensorflow.python.eager import execute as _execute
from tensorflow.python.framework import dtypes as _dtypes

from tensorflow.python.framework import op_def_registry as _op_def_registry
from tensorflow.python.framework import ops as _ops
from tensorflow.python.framework import op_def_library as _op_def_library
from tensorflow.python.util.deprecation import deprecated_endpoints
from tensorflow.python.util import dispatch as _dispatch
from tensorflow.python.util.tf_export import tf_export


def batch_cholesky(input, name=None):
  r"""TODO: add doc.

  Args:
    input: A `Tensor`. Must be one of the following types: `float64`, `float32`.
    name: A name for the operation (optional).

  Returns:
    A `Tensor`. Has the same type as `input`.
  """
  _ctx = _context._context or _context.context()
  tld = _ctx._thread_local_data
  if tld.is_eager:
    try:
      _result = pywrap_tfe.TFE_Py_FastPathExecute(
        _ctx._context_handle, tld.device_name, "BatchCholesky", name,
        tld.op_callbacks, input)
      return _result
    except _core._FallbackException:
      try:
        return batch_cholesky_eager_fallback(
            input, name=name, ctx=_ctx)
      except _core._SymbolicException:
        pass  # Add nodes to the TensorFlow graph.
    except _core._NotOkStatusException as e:
      _ops.raise_from_not_ok_status(e, name)
  # Add nodes to the TensorFlow graph.
  _, _, _op, _outputs = _op_def_library._apply_op_helper(
        "BatchCholesky", input=input, name=name)
  _result = _outputs[:]
  if _execute.must_record_gradient():
    _attrs = ("T", _op._get_attr_type("T"))
    _inputs_flat = _op.inputs
    _execute.record_gradient(
        "BatchCholesky", _inputs_flat, _attrs, _result)
  _result, = _result
  return _result

BatchCholesky = tf_export("raw_ops.BatchCholesky")(_ops.to_raw_op(batch_cholesky))


def batch_cholesky_eager_fallback(input, name, ctx):
  _attr_T, (input,) = _execute.args_to_matching_eager([input], ctx)
  _inputs_flat = [input]
  _attrs = ("T", _attr_T)
  _result = _execute.execute(b"BatchCholesky", 1, inputs=_inputs_flat,
                             attrs=_attrs, ctx=ctx, name=name)
  if _execute.must_record_gradient():
    _execute.record_gradient(
        "BatchCholesky", _inputs_flat, _attrs, _result)
  _result, = _result
  return _result


def batch_cholesky_grad(l, grad, name=None):
  r"""TODO: add doc.

  Args:
    l: A `Tensor`. Must be one of the following types: `float32`, `float64`.
    grad: A `Tensor`. Must have the same type as `l`.
    name: A name for the operation (optional).

  Returns:
    A `Tensor`. Has the same type as `l`.
  """
  _ctx = _context._context or _context.context()
  tld = _ctx._thread_local_data
  if tld.is_eager:
    try:
      _result = pywrap_tfe.TFE_Py_FastPathExecute(
        _ctx._context_handle, tld.device_name, "BatchCholeskyGrad", name,
        tld.op_callbacks, l, grad)
      return _result
    except _core._FallbackException:
      try:
        return batch_cholesky_grad_eager_fallback(
            l, grad, name=name, ctx=_ctx)
      except _core._SymbolicException:
        pass  # Add nodes to the TensorFlow graph.
    except _core._NotOkStatusException as e:
      _ops.raise_from_not_ok_status(e, name)
  # Add nodes to the TensorFlow graph.
  _, _, _op, _outputs = _op_def_library._apply_op_helper(
        "BatchCholeskyGrad", l=l, grad=grad, name=name)
  _result = _outputs[:]
  if _execute.must_record_gradient():
    _attrs = ("T", _op._get_attr_type("T"))
    _inputs_flat = _op.inputs
    _execute.record_gradient(
        "BatchCholeskyGrad", _inputs_flat, _attrs, _result)
  _result, = _result
  return _result

BatchCholeskyGrad = tf_export("raw_ops.BatchCholeskyGrad")(_ops.to_raw_op(batch_cholesky_grad))


def batch_cholesky_grad_eager_fallback(l, grad, name, ctx):
  _attr_T, _inputs_T = _execute.args_to_matching_eager([l, grad], ctx)
  (l, grad) = _inputs_T
  _inputs_flat = [l, grad]
  _attrs = ("T", _attr_T)
  _result = _execute.execute(b"BatchCholeskyGrad", 1, inputs=_inputs_flat,
                             attrs=_attrs, ctx=ctx, name=name)
  if _execute.must_record_gradient():
    _execute.record_gradient(
        "BatchCholeskyGrad", _inputs_flat, _attrs, _result)
  _result, = _result
  return _result


def batch_matrix_determinant(input, name=None):
  r"""TODO: add doc.

  Args:
    input: A `Tensor`. Must be one of the following types: `float32`, `float64`, `complex64`, `complex128`.
    name: A name for the operation (optional).

  Returns:
    A `Tensor`. Has the same type as `input`.
  """
  _ctx = _context._context or _context.context()
  tld = _ctx._thread_local_data
  if tld.is_eager:
    try:
      _result = pywrap_tfe.TFE_Py_FastPathExecute(
        _ctx._context_handle, tld.device_name, "BatchMatrixDeterminant", name,
        tld.op_callbacks, input)
      return _result
    except _core._FallbackException:
      try:
        return batch_matrix_determinant_eager_fallback(
            input, name=name, ctx=_ctx)
      except _core._SymbolicException:
        pass  # Add nodes to the TensorFlow graph.
    except _core._NotOkStatusException as e:
      _ops.raise_from_not_ok_status(e, name)
  # Add nodes to the TensorFlow graph.
  _, _, _op, _outputs = _op_def_library._apply_op_helper(
        "BatchMatrixDeterminant", input=input, name=name)
  _result = _outputs[:]
  if _execute.must_record_gradient():
    _attrs = ("T", _op._get_attr_type("T"))
    _inputs_flat = _op.inputs
    _execute.record_gradient(
        "BatchMatrixDeterminant", _inputs_flat, _attrs, _result)
  _result, = _result
  return _result

BatchMatrixDeterminant = tf_export("raw_ops.BatchMatrixDeterminant")(_ops.to_raw_op(batch_matrix_determinant))


def batch_matrix_determinant_eager_fallback(input, name, ctx):
  _attr_T, (input,) = _execute.args_to_matching_eager([input], ctx)
  _inputs_flat = [input]
  _attrs = ("T", _attr_T)
  _result = _execute.execute(b"BatchMatrixDeterminant", 1,
                             inputs=_inputs_flat, attrs=_attrs, ctx=ctx,
                             name=name)
  if _execute.must_record_gradient():
    _execute.record_gradient(
        "BatchMatrixDeterminant", _inputs_flat, _attrs, _result)
  _result, = _result
  return _result


def batch_matrix_inverse(input, adjoint=False, name=None):
  r"""TODO: add doc.

  Args:
    input: A `Tensor`. Must be one of the following types: `float64`, `float32`.
    adjoint: An optional `bool`. Defaults to `False`.
    name: A name for the operation (optional).

  Returns:
    A `Tensor`. Has the same type as `input`.
  """
  _ctx = _context._context or _context.context()
  tld = _ctx._thread_local_data
  if tld.is_eager:
    try:
      _result = pywrap_tfe.TFE_Py_FastPathExecute(
        _ctx._context_handle, tld.device_name, "BatchMatrixInverse", name,
        tld.op_callbacks, input, "adjoint", adjoint)
      return _result
    except _core._FallbackException:
      try:
        return batch_matrix_inverse_eager_fallback(
            input, adjoint=adjoint, name=name, ctx=_ctx)
      except _core._SymbolicException:
        pass  # Add nodes to the TensorFlow graph.
    except _core._NotOkStatusException as e:
      _ops.raise_from_not_ok_status(e, name)
  # Add nodes to the TensorFlow graph.
  if adjoint is None:
    adjoint = False
  adjoint = _execute.make_bool(adjoint, "adjoint")
  _, _, _op, _outputs = _op_def_library._apply_op_helper(
        "BatchMatrixInverse", input=input, adjoint=adjoint, name=name)
  _result = _outputs[:]
  if _execute.must_record_gradient():
    _attrs = ("adjoint", _op._get_attr_bool("adjoint"), "T",
              _op._get_attr_type("T"))
    _inputs_flat = _op.inputs
    _execute.record_gradient(
        "BatchMatrixInverse", _inputs_flat, _attrs, _result)
  _result, = _result
  return _result

BatchMatrixInverse = tf_export("raw_ops.BatchMatrixInverse")(_ops.to_raw_op(batch_matrix_inverse))


def batch_matrix_inverse_eager_fallback(input, adjoint, name, ctx):
  if adjoint is None:
    adjoint = False
  adjoint = _execute.make_bool(adjoint, "adjoint")
  _attr_T, (input,) = _execute.args_to_matching_eager([input], ctx)
  _inputs_flat = [input]
  _attrs = ("adjoint", adjoint, "T", _attr_T)
  _result = _execute.execute(b"BatchMatrixInverse", 1, inputs=_inputs_flat,
                             attrs=_attrs, ctx=ctx, name=name)
  if _execute.must_record_gradient():
    _execute.record_gradient(
        "BatchMatrixInverse", _inputs_flat, _attrs, _result)
  _result, = _result
  return _result


def batch_matrix_solve(matrix, rhs, adjoint=False, name=None):
  r"""TODO: add doc.

  Args:
    matrix: A `Tensor`. Must be one of the following types: `float64`, `float32`.
    rhs: A `Tensor`. Must have the same type as `matrix`.
    adjoint: An optional `bool`. Defaults to `False`.
    name: A name for the operation (optional).

  Returns:
    A `Tensor`. Has the same type as `matrix`.
  """
  _ctx = _context._context or _context.context()
  tld = _ctx._thread_local_data
  if tld.is_eager:
    try:
      _result = pywrap_tfe.TFE_Py_FastPathExecute(
        _ctx._context_handle, tld.device_name, "BatchMatrixSolve", name,
        tld.op_callbacks, matrix, rhs, "adjoint", adjoint)
      return _result
    except _core._FallbackException:
      try:
        return batch_matrix_solve_eager_fallback(
            matrix, rhs, adjoint=adjoint, name=name, ctx=_ctx)
      except _core._SymbolicException:
        pass  # Add nodes to the TensorFlow graph.
    except _core._NotOkStatusException as e:
      _ops.raise_from_not_ok_status(e, name)
  # Add nodes to the TensorFlow graph.
  if adjoint is None:
    adjoint = False
  adjoint = _execute.make_bool(adjoint, "adjoint")
  _, _, _op, _outputs = _op_def_library._apply_op_helper(
        "BatchMatrixSolve", matrix=matrix, rhs=rhs, adjoint=adjoint,
                            name=name)
  _result = _outputs[:]
  if _execute.must_record_gradient():
    _attrs = ("adjoint", _op._get_attr_bool("adjoint"), "T",
              _op._get_attr_type("T"))
    _inputs_flat = _op.inputs
    _execute.record_gradient(
        "BatchMatrixSolve", _inputs_flat, _attrs, _result)
  _result, = _result
  return _result

BatchMatrixSolve = tf_export("raw_ops.BatchMatrixSolve")(_ops.to_raw_op(batch_matrix_solve))


def batch_matrix_solve_eager_fallback(matrix, rhs, adjoint, name, ctx):
  if adjoint is None:
    adjoint = False
  adjoint = _execute.make_bool(adjoint, "adjoint")
  _attr_T, _inputs_T = _execute.args_to_matching_eager([matrix, rhs], ctx)
  (matrix, rhs) = _inputs_T
  _inputs_flat = [matrix, rhs]
  _attrs = ("adjoint", adjoint, "T", _attr_T)
  _result = _execute.execute(b"BatchMatrixSolve", 1, inputs=_inputs_flat,
                             attrs=_attrs, ctx=ctx, name=name)
  if _execute.must_record_gradient():
    _execute.record_gradient(
        "BatchMatrixSolve", _inputs_flat, _attrs, _result)
  _result, = _result
  return _result


def batch_matrix_solve_ls(matrix, rhs, l2_regularizer, fast=True, name=None):
  r"""TODO: add doc.

  Args:
    matrix: A `Tensor`. Must be one of the following types: `float64`, `float32`.
    rhs: A `Tensor`. Must have the same type as `matrix`.
    l2_regularizer: A `Tensor` of type `float64`.
    fast: An optional `bool`. Defaults to `True`.
    name: A name for the operation (optional).

  Returns:
    A `Tensor`. Has the same type as `matrix`.
  """
  _ctx = _context._context or _context.context()
  tld = _ctx._thread_local_data
  if tld.is_eager:
    try:
      _result = pywrap_tfe.TFE_Py_FastPathExecute(
        _ctx._context_handle, tld.device_name, "BatchMatrixSolveLs", name,
        tld.op_callbacks, matrix, rhs, l2_regularizer, "fast", fast)
      return _result
    except _core._FallbackException:
      try:
        return batch_matrix_solve_ls_eager_fallback(
            matrix, rhs, l2_regularizer, fast=fast, name=name, ctx=_ctx)
      except _core._SymbolicException:
        pass  # Add nodes to the TensorFlow graph.
    except _core._NotOkStatusException as e:
      _ops.raise_from_not_ok_status(e, name)
  # Add nodes to the TensorFlow graph.
  if fast is None:
    fast = True
  fast = _execute.make_bool(fast, "fast")
  _, _, _op, _outputs = _op_def_library._apply_op_helper(
        "BatchMatrixSolveLs", matrix=matrix, rhs=rhs,
                              l2_regularizer=l2_regularizer, fast=fast,
                              name=name)
  _result = _outputs[:]
  if _execute.must_record_gradient():
    _attrs = ("T", _op._get_attr_type("T"), "fast",
              _op._get_attr_bool("fast"))
    _inputs_flat = _op.inputs
    _execute.record_gradient(
        "BatchMatrixSolveLs", _inputs_flat, _attrs, _result)
  _result, = _result
  return _result

BatchMatrixSolveLs = tf_export("raw_ops.BatchMatrixSolveLs")(_ops.to_raw_op(batch_matrix_solve_ls))


def batch_matrix_solve_ls_eager_fallback(matrix, rhs, l2_regularizer, fast, name, ctx):
  if fast is None:
    fast = True
  fast = _execute.make_bool(fast, "fast")
  _attr_T, _inputs_T = _execute.args_to_matching_eager([matrix, rhs], ctx)
  (matrix, rhs) = _inputs_T
  l2_regularizer = _ops.convert_to_tensor(l2_regularizer, _dtypes.float64)
  _inputs_flat = [matrix, rhs, l2_regularizer]
  _attrs = ("T", _attr_T, "fast", fast)
  _result = _execute.execute(b"BatchMatrixSolveLs", 1, inputs=_inputs_flat,
                             attrs=_attrs, ctx=ctx, name=name)
  if _execute.must_record_gradient():
    _execute.record_gradient(
        "BatchMatrixSolveLs", _inputs_flat, _attrs, _result)
  _result, = _result
  return _result


def batch_matrix_triangular_solve(matrix, rhs, lower=True, adjoint=False, name=None):
  r"""TODO: add doc.

  Args:
    matrix: A `Tensor`. Must be one of the following types: `float64`, `float32`.
    rhs: A `Tensor`. Must have the same type as `matrix`.
    lower: An optional `bool`. Defaults to `True`.
    adjoint: An optional `bool`. Defaults to `False`.
    name: A name for the operation (optional).

  Returns:
    A `Tensor`. Has the same type as `matrix`.
  """
  _ctx = _context._context or _context.context()
  tld = _ctx._thread_local_data
  if tld.is_eager:
    try:
      _result = pywrap_tfe.TFE_Py_FastPathExecute(
        _ctx._context_handle, tld.device_name, "BatchMatrixTriangularSolve",
        name, tld.op_callbacks, matrix, rhs, "lower", lower, "adjoint",
        adjoint)
      return _result
    except _core._FallbackException:
      try:
        return batch_matrix_triangular_solve_eager_fallback(
            matrix, rhs, lower=lower, adjoint=adjoint, name=name, ctx=_ctx)
      except _core._SymbolicException:
        pass  # Add nodes to the TensorFlow graph.
    except _core._NotOkStatusException as e:
      _ops.raise_from_not_ok_status(e, name)
  # Add nodes to the TensorFlow graph.
  if lower is None:
    lower = True
  lower = _execute.make_bool(lower, "lower")
  if adjoint is None:
    adjoint = False
  adjoint = _execute.make_bool(adjoint, "adjoint")
  _, _, _op, _outputs = _op_def_library._apply_op_helper(
        "BatchMatrixTriangularSolve", matrix=matrix, rhs=rhs, lower=lower,
                                      adjoint=adjoint, name=name)
  _result = _outputs[:]
  if _execute.must_record_gradient():
    _attrs = ("lower", _op._get_attr_bool("lower"), "adjoint",
              _op._get_attr_bool("adjoint"), "T", _op._get_attr_type("T"))
    _inputs_flat = _op.inputs
    _execute.record_gradient(
        "BatchMatrixTriangularSolve", _inputs_flat, _attrs, _result)
  _result, = _result
  return _result

BatchMatrixTriangularSolve = tf_export("raw_ops.BatchMatrixTriangularSolve")(_ops.to_raw_op(batch_matrix_triangular_solve))


def batch_matrix_triangular_solve_eager_fallback(matrix, rhs, lower, adjoint, name, ctx):
  if lower is None:
    lower = True
  lower = _execute.make_bool(lower, "lower")
  if adjoint is None:
    adjoint = False
  adjoint = _execute.make_bool(adjoint, "adjoint")
  _attr_T, _inputs_T = _execute.args_to_matching_eager([matrix, rhs], ctx)
  (matrix, rhs) = _inputs_T
  _inputs_flat = [matrix, rhs]
  _attrs = ("lower", lower, "adjoint", adjoint, "T", _attr_T)
  _result = _execute.execute(b"BatchMatrixTriangularSolve", 1,
                             inputs=_inputs_flat, attrs=_attrs, ctx=ctx,
                             name=name)
  if _execute.must_record_gradient():
    _execute.record_gradient(
        "BatchMatrixTriangularSolve", _inputs_flat, _attrs, _result)
  _result, = _result
  return _result


def batch_self_adjoint_eig(input, name=None):
  r"""TODO: add doc.

  Args:
    input: A `Tensor`. Must be one of the following types: `float64`, `float32`.
    name: A name for the operation (optional).

  Returns:
    A `Tensor`. Has the same type as `input`.
  """
  _ctx = _context._context or _context.context()
  tld = _ctx._thread_local_data
  if tld.is_eager:
    try:
      _result = pywrap_tfe.TFE_Py_FastPathExecute(
        _ctx._context_handle, tld.device_name, "BatchSelfAdjointEig", name,
        tld.op_callbacks, input)
      return _result
    except _core._FallbackException:
      try:
        return batch_self_adjoint_eig_eager_fallback(
            input, name=name, ctx=_ctx)
      except _core._SymbolicException:
        pass  # Add nodes to the TensorFlow graph.
    except _core._NotOkStatusException as e:
      _ops.raise_from_not_ok_status(e, name)
  # Add nodes to the TensorFlow graph.
  _, _, _op, _outputs = _op_def_library._apply_op_helper(
        "BatchSelfAdjointEig", input=input, name=name)
  _result = _outputs[:]
  if _execute.must_record_gradient():
    _attrs = ("T", _op._get_attr_type("T"))
    _inputs_flat = _op.inputs
    _execute.record_gradient(
        "BatchSelfAdjointEig", _inputs_flat, _attrs, _result)
  _result, = _result
  return _result

BatchSelfAdjointEig = tf_export("raw_ops.BatchSelfAdjointEig")(_ops.to_raw_op(batch_self_adjoint_eig))


def batch_self_adjoint_eig_eager_fallback(input, name, ctx):
  _attr_T, (input,) = _execute.args_to_matching_eager([input], ctx)
  _inputs_flat = [input]
  _attrs = ("T", _attr_T)
  _result = _execute.execute(b"BatchSelfAdjointEig", 1, inputs=_inputs_flat,
                             attrs=_attrs, ctx=ctx, name=name)
  if _execute.must_record_gradient():
    _execute.record_gradient(
        "BatchSelfAdjointEig", _inputs_flat, _attrs, _result)
  _result, = _result
  return _result

_BatchSelfAdjointEigV2Output = collections.namedtuple(
    "BatchSelfAdjointEigV2",
    ["e", "v"])


def batch_self_adjoint_eig_v2(input, compute_v=True, name=None):
  r"""TODO: add doc.

  Args:
    input: A `Tensor`. Must be one of the following types: `float64`, `float32`.
    compute_v: An optional `bool`. Defaults to `True`.
    name: A name for the operation (optional).

  Returns:
    A tuple of `Tensor` objects (e, v).

    e: A `Tensor`. Has the same type as `input`.
    v: A `Tensor`. Has the same type as `input`.
  """
  _ctx = _context._context or _context.context()
  tld = _ctx._thread_local_data
  if tld.is_eager:
    try:
      _result = pywrap_tfe.TFE_Py_FastPathExecute(
        _ctx._context_handle, tld.device_name, "BatchSelfAdjointEigV2", name,
        tld.op_callbacks, input, "compute_v", compute_v)
      _result = _BatchSelfAdjointEigV2Output._make(_result)
      return _result
    except _core._FallbackException:
      try:
        return batch_self_adjoint_eig_v2_eager_fallback(
            input, compute_v=compute_v, name=name, ctx=_ctx)
      except _core._SymbolicException:
        pass  # Add nodes to the TensorFlow graph.
    except _core._NotOkStatusException as e:
      _ops.raise_from_not_ok_status(e, name)
  # Add nodes to the TensorFlow graph.
  if compute_v is None:
    compute_v = True
  compute_v = _execute.make_bool(compute_v, "compute_v")
  _, _, _op, _outputs = _op_def_library._apply_op_helper(
        "BatchSelfAdjointEigV2", input=input, compute_v=compute_v, name=name)
  _result = _outputs[:]
  if _execute.must_record_gradient():
    _attrs = ("compute_v", _op._get_attr_bool("compute_v"), "T",
              _op._get_attr_type("T"))
    _inputs_flat = _op.inputs
    _execute.record_gradient(
        "BatchSelfAdjointEigV2", _inputs_flat, _attrs, _result)
  _result = _BatchSelfAdjointEigV2Output._make(_result)
  return _result

BatchSelfAdjointEigV2 = tf_export("raw_ops.BatchSelfAdjointEigV2")(_ops.to_raw_op(batch_self_adjoint_eig_v2))


def batch_self_adjoint_eig_v2_eager_fallback(input, compute_v, name, ctx):
  if compute_v is None:
    compute_v = True
  compute_v = _execute.make_bool(compute_v, "compute_v")
  _attr_T, (input,) = _execute.args_to_matching_eager([input], ctx)
  _inputs_flat = [input]
  _attrs = ("compute_v", compute_v, "T", _attr_T)
  _result = _execute.execute(b"BatchSelfAdjointEigV2", 2, inputs=_inputs_flat,
                             attrs=_attrs, ctx=ctx, name=name)
  if _execute.must_record_gradient():
    _execute.record_gradient(
        "BatchSelfAdjointEigV2", _inputs_flat, _attrs, _result)
  _result = _BatchSelfAdjointEigV2Output._make(_result)
  return _result

_BatchSvdOutput = collections.namedtuple(
    "BatchSvd",
    ["s", "u", "v"])


def batch_svd(input, compute_uv=True, full_matrices=False, name=None):
  r"""TODO: add doc.

  Args:
    input: A `Tensor`. Must be one of the following types: `float64`, `float32`, `complex64`, `complex128`.
    compute_uv: An optional `bool`. Defaults to `True`.
    full_matrices: An optional `bool`. Defaults to `False`.
    name: A name for the operation (optional).

  Returns:
    A tuple of `Tensor` objects (s, u, v).

    s: A `Tensor`. Has the same type as `input`.
    u: A `Tensor`. Has the same type as `input`.
    v: A `Tensor`. Has the same type as `input`.
  """
  _ctx = _context._context or _context.context()
  tld = _ctx._thread_local_data
  if tld.is_eager:
    try:
      _result = pywrap_tfe.TFE_Py_FastPathExecute(
        _ctx._context_handle, tld.device_name, "BatchSvd", name,
        tld.op_callbacks, input, "compute_uv", compute_uv, "full_matrices",
        full_matrices)
      _result = _BatchSvdOutput._make(_result)
      return _result
    except _core._FallbackException:
      try:
        return batch_svd_eager_fallback(
            input, compute_uv=compute_uv, full_matrices=full_matrices,
            name=name, ctx=_ctx)
      except _core._SymbolicException:
        pass  # Add nodes to the TensorFlow graph.
    except _core._NotOkStatusException as e:
      _ops.raise_from_not_ok_status(e, name)
  # Add nodes to the TensorFlow graph.
  if compute_uv is None:
    compute_uv = True
  compute_uv = _execute.make_bool(compute_uv, "compute_uv")
  if full_matrices is None:
    full_matrices = False
  full_matrices = _execute.make_bool(full_matrices, "full_matrices")
  _, _, _op, _outputs = _op_def_library._apply_op_helper(
        "BatchSvd", input=input, compute_uv=compute_uv,
                    full_matrices=full_matrices, name=name)
  _result = _outputs[:]
  if _execute.must_record_gradient():
    _attrs = ("compute_uv", _op._get_attr_bool("compute_uv"), "full_matrices",
              _op._get_attr_bool("full_matrices"), "T",
              _op._get_attr_type("T"))
    _inputs_flat = _op.inputs
    _execute.record_gradient(
        "BatchSvd", _inputs_flat, _attrs, _result)
  _result = _BatchSvdOutput._make(_result)
  return _result

BatchSvd = tf_export("raw_ops.BatchSvd")(_ops.to_raw_op(batch_svd))


def batch_svd_eager_fallback(input, compute_uv, full_matrices, name, ctx):
  if compute_uv is None:
    compute_uv = True
  compute_uv = _execute.make_bool(compute_uv, "compute_uv")
  if full_matrices is None:
    full_matrices = False
  full_matrices = _execute.make_bool(full_matrices, "full_matrices")
  _attr_T, (input,) = _execute.args_to_matching_eager([input], ctx)
  _inputs_flat = [input]
  _attrs = ("compute_uv", compute_uv, "full_matrices", full_matrices, "T",
  _attr_T)
  _result = _execute.execute(b"BatchSvd", 3, inputs=_inputs_flat,
                             attrs=_attrs, ctx=ctx, name=name)
  if _execute.must_record_gradient():
    _execute.record_gradient(
        "BatchSvd", _inputs_flat, _attrs, _result)
  _result = _BatchSvdOutput._make(_result)
  return _result


@_dispatch.add_dispatch_list
@tf_export('linalg.cholesky', v1=['linalg.cholesky', 'cholesky'])
@deprecated_endpoints('cholesky')
def cholesky(input, name=None):
  r"""Computes the Cholesky decomposition of one or more square matrices.

  The input is a tensor of shape `[..., M, M]` whose inner-most 2 dimensions
  form square matrices.

  The input has to be symmetric and positive definite. Only the lower-triangular
  part of the input will be used for this operation. The upper-triangular part
  will not be read.

  The output is a tensor of the same shape as the input
  containing the Cholesky decompositions for all input submatrices `[..., :, :]`.

  **Note**: The gradient computation on GPU is faster for large matrices but
  not for large batch dimensions when the submatrices are small. In this
  case it might be faster to use the CPU.

  Args:
    input: A `Tensor`. Must be one of the following types: `float64`, `float32`, `half`, `complex64`, `complex128`.
      Shape is `[..., M, M]`.
    name: A name for the operation (optional).

  Returns:
    A `Tensor`. Has the same type as `input`.
  """
  _ctx = _context._context or _context.context()
  tld = _ctx._thread_local_data
  if tld.is_eager:
    try:
      _result = pywrap_tfe.TFE_Py_FastPathExecute(
        _ctx._context_handle, tld.device_name, "Cholesky", name,
        tld.op_callbacks, input)
      return _result
    except _core._FallbackException:
      try:
        return cholesky_eager_fallback(
            input, name=name, ctx=_ctx)
      except _core._SymbolicException:
        pass  # Add nodes to the TensorFlow graph.
      except (TypeError, ValueError):
        result = _dispatch.dispatch(
              cholesky, input=input, name=name)
        if result is not _dispatch.OpDispatcher.NOT_SUPPORTED:
          return result
        raise
    except _core._NotOkStatusException as e:
      _ops.raise_from_not_ok_status(e, name)
  # Add nodes to the TensorFlow graph.
  try:
    _, _, _op, _outputs = _op_def_library._apply_op_helper(
        "Cholesky", input=input, name=name)
  except (TypeError, ValueError):
    result = _dispatch.dispatch(
          cholesky, input=input, name=name)
    if result is not _dispatch.OpDispatcher.NOT_SUPPORTED:
      return result
    raise
  _result = _outputs[:]
  if _execute.must_record_gradient():
    _attrs = ("T", _op._get_attr_type("T"))
    _inputs_flat = _op.inputs
    _execute.record_gradient(
        "Cholesky", _inputs_flat, _attrs, _result)
  _result, = _result
  return _result

Cholesky = tf_export("raw_ops.Cholesky")(_ops.to_raw_op(cholesky))


def cholesky_eager_fallback(input, name, ctx):
  _attr_T, (input,) = _execute.args_to_matching_eager([input], ctx)
  _inputs_flat = [input]
  _attrs = ("T", _attr_T)
  _result = _execute.execute(b"Cholesky", 1, inputs=_inputs_flat,
                             attrs=_attrs, ctx=ctx, name=name)
  if _execute.must_record_gradient():
    _execute.record_gradient(
        "Cholesky", _inputs_flat, _attrs, _result)
  _result, = _result
  return _result


def cholesky_grad(l, grad, name=None):
  r"""Computes the reverse mode backpropagated gradient of the Cholesky algorithm.

  For an explanation see "Differentiation of the Cholesky algorithm" by
  Iain Murray http://arxiv.org/abs/1602.07527.

  Args:
    l: A `Tensor`. Must be one of the following types: `half`, `float32`, `float64`.
      Output of batch Cholesky algorithm l = cholesky(A). Shape is `[..., M, M]`.
      Algorithm depends only on lower triangular part of the innermost matrices of
      this tensor.
    grad: A `Tensor`. Must have the same type as `l`.
      df/dl where f is some scalar function. Shape is `[..., M, M]`.
      Algorithm depends only on lower triangular part of the innermost matrices of
      this tensor.
    name: A name for the operation (optional).

  Returns:
    A `Tensor`. Has the same type as `l`.
  """
  _ctx = _context._context or _context.context()
  tld = _ctx._thread_local_data
  if tld.is_eager:
    try:
      _result = pywrap_tfe.TFE_Py_FastPathExecute(
        _ctx._context_handle, tld.device_name, "CholeskyGrad", name,
        tld.op_callbacks, l, grad)
      return _result
    except _core._FallbackException:
      try:
        return cholesky_grad_eager_fallback(
            l, grad, name=name, ctx=_ctx)
      except _core._SymbolicException:
        pass  # Add nodes to the TensorFlow graph.
    except _core._NotOkStatusException as e:
      _ops.raise_from_not_ok_status(e, name)
  # Add nodes to the TensorFlow graph.
  _, _, _op, _outputs = _op_def_library._apply_op_helper(
        "CholeskyGrad", l=l, grad=grad, name=name)
  _result = _outputs[:]
  if _execute.must_record_gradient():
    _attrs = ("T", _op._get_attr_type("T"))
    _inputs_flat = _op.inputs
    _execute.record_gradient(
        "CholeskyGrad", _inputs_flat, _attrs, _result)
  _result, = _result
  return _result

CholeskyGrad = tf_export("raw_ops.CholeskyGrad")(_ops.to_raw_op(cholesky_grad))


def cholesky_grad_eager_fallback(l, grad, name, ctx):
  _attr_T, _inputs_T = _execute.args_to_matching_eager([l, grad], ctx)
  (l, grad) = _inputs_T
  _inputs_flat = [l, grad]
  _attrs = ("T", _attr_T)
  _result = _execute.execute(b"CholeskyGrad", 1, inputs=_inputs_flat,
                             attrs=_attrs, ctx=ctx, name=name)
  if _execute.must_record_gradient():
    _execute.record_gradient(
        "CholeskyGrad", _inputs_flat, _attrs, _result)
  _result, = _result
  return _result

_EigOutput = collections.namedtuple(
    "Eig",
    ["e", "v"])


def eig(input, Tout, compute_v=True, name=None):
  r"""Computes the eigen decomposition of one or more square matrices.

  Computes the eigenvalues and (optionally) right eigenvectors of each inner matrix in
  `input` such that `input[..., :, :] = v[..., :, :] * diag(e[..., :])`. The eigenvalues
  are sorted in non-decreasing order.

  ```python
  # a is a tensor.
  # e is a tensor of eigenvalues.
  # v is a tensor of eigenvectors.
  e, v = eig(a)
  e = eig(a, compute_v=False)
  ```

  Args:
    input: A `Tensor`. Must be one of the following types: `float32`, `float64`, `complex64`, `complex128`.
      `Tensor` input of shape `[N, N]`.
    Tout: A `tf.DType` from: `tf.complex64, tf.complex128`.
    compute_v: An optional `bool`. Defaults to `True`.
      If `True` then eigenvectors will be computed and returned in `v`.
      Otherwise, only the eigenvalues will be computed.
    name: A name for the operation (optional).

  Returns:
    A tuple of `Tensor` objects (e, v).

    e: A `Tensor` of type `Tout`.
    v: A `Tensor` of type `Tout`.
  """
  _ctx = _context._context or _context.context()
  tld = _ctx._thread_local_data
  if tld.is_eager:
    try:
      _result = pywrap_tfe.TFE_Py_FastPathExecute(
        _ctx._context_handle, tld.device_name, "Eig", name, tld.op_callbacks,
        input, "compute_v", compute_v, "Tout", Tout)
      _result = _EigOutput._make(_result)
      return _result
    except _core._FallbackException:
      try:
        return eig_eager_fallback(
            input, compute_v=compute_v, Tout=Tout, name=name, ctx=_ctx)
      except _core._SymbolicException:
        pass  # Add nodes to the TensorFlow graph.
    except _core._NotOkStatusException as e:
      _ops.raise_from_not_ok_status(e, name)
  # Add nodes to the TensorFlow graph.
  Tout = _execute.make_type(Tout, "Tout")
  if compute_v is None:
    compute_v = True
  compute_v = _execute.make_bool(compute_v, "compute_v")
  _, _, _op, _outputs = _op_def_library._apply_op_helper(
        "Eig", input=input, Tout=Tout, compute_v=compute_v, name=name)
  _result = _outputs[:]
  if _execute.must_record_gradient():
    _attrs = ("compute_v", _op._get_attr_bool("compute_v"), "T",
              _op._get_attr_type("T"), "Tout", _op._get_attr_type("Tout"))
    _inputs_flat = _op.inputs
    _execute.record_gradient(
        "Eig", _inputs_flat, _attrs, _result)
  _result = _EigOutput._make(_result)
  return _result

Eig = tf_export("raw_ops.Eig")(_ops.to_raw_op(eig))


def eig_eager_fallback(input, Tout, compute_v, name, ctx):
  Tout = _execute.make_type(Tout, "Tout")
  if compute_v is None:
    compute_v = True
  compute_v = _execute.make_bool(compute_v, "compute_v")
  _attr_T, (input,) = _execute.args_to_matching_eager([input], ctx)
  _inputs_flat = [input]
  _attrs = ("compute_v", compute_v, "T", _attr_T, "Tout", Tout)
  _result = _execute.execute(b"Eig", 2, inputs=_inputs_flat, attrs=_attrs,
                             ctx=ctx, name=name)
  if _execute.must_record_gradient():
    _execute.record_gradient(
        "Eig", _inputs_flat, _attrs, _result)
  _result = _EigOutput._make(_result)
  return _result


def einsum(inputs, equation, name=None):
  r"""Tensor contraction according to Einstein summation convention.

  Implements generalized Tensor contraction and reduction. Each input Tensor must
  have a corresponding input subscript appearing in the comma-separated left-hand
  side of the equation. The right-hand side of the equation consists of the
  output subscript. The input subscripts and the output subscript should consist
  of zero or more named axis labels and at most one ellipsis (`...`).

  The named axis labels may be any single character other than those having
  special meaning, namely `,.->`. The behavior of this Op is undefined if it
  receives an ill-formatted equation; since the validation is done at
  graph-building time, we omit format validation checks at runtime.

  Note: This Op is *not* intended to be called by the user; instead users should
  call `tf.einsum` directly. It is a hidden Op used by `tf.einsum`.

  Operations are applied to the input(s) according to the following rules:

   (a) Generalized Diagonals: For input dimensions corresponding to axis labels
       appearing more than once in the same input subscript, we take the
       generalized (`k`-dimensional) diagonal.
       For example, in the equation `iii->i` with input shape `[3, 3, 3]`, the
       generalized diagonal would consist of `3` elements at indices `(0, 0, 0)`,
       `(1, 1, 1)` and `(2, 2, 2)` to create a Tensor of shape `[3]`.

   (b) Reduction: Axes corresponding to labels appearing only in one input
       subscript but not in the output subscript are summed over prior to Tensor
       contraction.
       For example, in the equation `ab,bc->b`, the axis labels `a` and `c` are
       the reduction axis labels.

   (c) Batch Dimensions: Axes corresponding to labels appearing in each of the
       input subscripts and also in the output subscript make up the batch
       dimensions in Tensor contraction. Unnamed axis labels corresponding to
       ellipsis (`...`) also correspond to batch dimensions.
       For example, for the equation denoting batch matrix multiplication,
       `bij,bjk->bik`, the axis label `b` corresponds to a batch dimension.

   (d) Contraction: In case of binary einsum, axes corresponding to labels
       appearing in two different inputs (and not in the output) are contracted
       against each other.
       Considering the batch matrix multiplication equation again
       (`bij,bjk->bik`), the contracted axis label is `j`.

   (e) Expand Diagonal: If the output subscripts contain repeated (explicit) axis
       labels, the opposite operation of (a) is applied. For example, in the
       equation `i->iii`, and input shape `[3]`, the output of shape `[3, 3, 3]`
       are all zeros, except for the (generalized) diagonal which is populated
       with values from the input.
       Note: This operation is not supported by `np.einsum` or `tf.einsum`; it is
       provided to enable computing the symbolic gradient of `tf.einsum`.

  The output subscripts must contain only labels appearing in at least one of the
  input subscripts. Furthermore, all dimensions mapping to the same axis label
  must be equal.

  Any of the input and output subscripts may contain at most a single ellipsis
  (`...`). These ellipsis are mapped against dimensions not corresponding to any
  named axis label. If two inputs contain ellipsis, then they are broadcasted
  according to standard NumPy broadcasting
  [rules](http://docs.scipy.org/doc/numpy/user/basics.broadcasting.html).

  The broadcasted dimensions are placed in the corresponding location of the
  ellipsis in the output subscript. If the broadcasted dimensions are non-empty
  and the output subscripts do not contain ellipsis, then an InvalidArgument error
  is raised.

  @compatibility(numpy)
  Similar to [`numpy.einsum`](https://docs.scipy.org/doc/numpy/reference/generated/numpy.einsum.html).

  Comparison with `numpy.einsum`:

   * This Op only supports unary and binary forms of `numpy.einsum`.
   * This Op does not support implicit form. (i.e. equations without `->`).
   * This Op also supports repeated indices in the output subscript, which is not
     supported by `numpy.einsum`.
  @end_compatibility

  Args:
    inputs: A list of at least 1 `Tensor` objects with the same type.
      List of 1 or 2 Tensors.
    equation: A `string`.
      String describing the Einstein Summation operation; in the format of np.einsum.
    name: A name for the operation (optional).

  Returns:
    A `Tensor`. Has the same type as `inputs`.
  """
  _ctx = _context._context or _context.context()
  tld = _ctx._thread_local_data
  if tld.is_eager:
    try:
      _result = pywrap_tfe.TFE_Py_FastPathExecute(
        _ctx._context_handle, tld.device_name, "Einsum", name,
        tld.op_callbacks, inputs, "equation", equation)
      return _result
    except _core._FallbackException:
      try:
        return einsum_eager_fallback(
            inputs, equation=equation, name=name, ctx=_ctx)
      except _core._SymbolicException:
        pass  # Add nodes to the TensorFlow graph.
    except _core._NotOkStatusException as e:
      _ops.raise_from_not_ok_status(e, name)
  # Add nodes to the TensorFlow graph.
  if not isinstance(inputs, (list, tuple)):
    raise TypeError(
        "Expected list for 'inputs' argument to "
        "'einsum' Op, not %r." % inputs)
  _attr_N = len(inputs)
  equation = _execute.make_str(equation, "equation")
  _, _, _op, _outputs = _op_def_library._apply_op_helper(
        "Einsum", inputs=inputs, equation=equation, name=name)
  _result = _outputs[:]
  if _execute.must_record_gradient():
    _attrs = ("equation", _op.get_attr("equation"), "N",
              _op._get_attr_int("N"), "T", _op._get_attr_type("T"))
    _inputs_flat = _op.inputs
    _execute.record_gradient(
        "Einsum", _inputs_flat, _attrs, _result)
  _result, = _result
  return _result

Einsum = tf_export("raw_ops.Einsum")(_ops.to_raw_op(einsum))


def einsum_eager_fallback(inputs, equation, name, ctx):
  if not isinstance(inputs, (list, tuple)):
    raise TypeError(
        "Expected list for 'inputs' argument to "
        "'einsum' Op, not %r." % inputs)
  _attr_N = len(inputs)
  equation = _execute.make_str(equation, "equation")
  _attr_T, inputs = _execute.args_to_matching_eager(list(inputs), ctx)
  _inputs_flat = list(inputs)
  _attrs = ("equation", equation, "N", _attr_N, "T", _attr_T)
  _result = _execute.execute(b"Einsum", 1, inputs=_inputs_flat, attrs=_attrs,
                             ctx=ctx, name=name)
  if _execute.must_record_gradient():
    _execute.record_gradient(
        "Einsum", _inputs_flat, _attrs, _result)
  _result, = _result
  return _result

_LogMatrixDeterminantOutput = collections.namedtuple(
    "LogMatrixDeterminant",
    ["sign", "log_abs_determinant"])


def log_matrix_determinant(input, name=None):
  r"""Computes the sign and the log of the absolute value of the determinant of

  one or more square matrices.

  The input is a tensor of shape `[N, M, M]` whose inner-most 2 dimensions
  form square matrices. The outputs are two tensors containing the signs and
  absolute values of the log determinants for all N input submatrices
  `[..., :, :]` such that the determinant = sign*exp(log_abs_determinant).
  The log_abs_determinant is computed as det(P)*sum(log(diag(LU))) where LU
  is the LU decomposition of the input and P is the corresponding
  permutation matrix.

  Args:
    input: A `Tensor`. Must be one of the following types: `half`, `float32`, `float64`, `complex64`, `complex128`.
      Shape is `[N, M, M]`.
    name: A name for the operation (optional).

  Returns:
    A tuple of `Tensor` objects (sign, log_abs_determinant).

    sign: A `Tensor`. Has the same type as `input`.
    log_abs_determinant: A `Tensor`. Has the same type as `input`.
  """
  _ctx = _context._context or _context.context()
  tld = _ctx._thread_local_data
  if tld.is_eager:
    try:
      _result = pywrap_tfe.TFE_Py_FastPathExecute(
        _ctx._context_handle, tld.device_name, "LogMatrixDeterminant", name,
        tld.op_callbacks, input)
      _result = _LogMatrixDeterminantOutput._make(_result)
      return _result
    except _core._FallbackException:
      try:
        return log_matrix_determinant_eager_fallback(
            input, name=name, ctx=_ctx)
      except _core._SymbolicException:
        pass  # Add nodes to the TensorFlow graph.
    except _core._NotOkStatusException as e:
      _ops.raise_from_not_ok_status(e, name)
  # Add nodes to the TensorFlow graph.
  _, _, _op, _outputs = _op_def_library._apply_op_helper(
        "LogMatrixDeterminant", input=input, name=name)
  _result = _outputs[:]
  if _execute.must_record_gradient():
    _attrs = ("T", _op._get_attr_type("T"))
    _inputs_flat = _op.inputs
    _execute.record_gradient(
        "LogMatrixDeterminant", _inputs_flat, _attrs, _result)
  _result = _LogMatrixDeterminantOutput._make(_result)
  return _result

LogMatrixDeterminant = tf_export("raw_ops.LogMatrixDeterminant")(_ops.to_raw_op(log_matrix_determinant))


def log_matrix_determinant_eager_fallback(input, name, ctx):
  _attr_T, (input,) = _execute.args_to_matching_eager([input], ctx)
  _inputs_flat = [input]
  _attrs = ("T", _attr_T)
  _result = _execute.execute(b"LogMatrixDeterminant", 2, inputs=_inputs_flat,
                             attrs=_attrs, ctx=ctx, name=name)
  if _execute.must_record_gradient():
    _execute.record_gradient(
        "LogMatrixDeterminant", _inputs_flat, _attrs, _result)
  _result = _LogMatrixDeterminantOutput._make(_result)
  return _result

_LuOutput = collections.namedtuple(
    "Lu",
    ["lu", "p"])


@_dispatch.add_dispatch_list
@tf_export('linalg.lu')
def lu(input, output_idx_type=_dtypes.int32, name=None):
  r"""Computes the LU decomposition of one or more square matrices.

  The input is a tensor of shape `[..., M, M]` whose inner-most 2 dimensions
  form square matrices.

  The input has to be invertible.

  The output consists of two tensors LU and P containing the LU decomposition
  of all input submatrices `[..., :, :]`. LU encodes the lower triangular and
  upper triangular factors.

  For each input submatrix of shape `[M, M]`, L is a lower triangular matrix of
  shape `[M, M]` with unit diagonal whose entries correspond to the strictly lower
  triangular part of LU. U is a upper triangular matrix of shape `[M, M]` whose
  entries correspond to the upper triangular part, including the diagonal, of LU.

  P represents a permutation matrix encoded as a list of indices each between `0`
  and `M-1`, inclusive. If P_mat denotes the permutation matrix corresponding to
  P, then the L, U and P satisfies P_mat * input = L * U.

  Args:
    input: A `Tensor`. Must be one of the following types: `float64`, `float32`, `half`, `complex64`, `complex128`.
      A tensor of shape `[..., M, M]` whose inner-most 2 dimensions form matrices of
      size `[M, M]`.
    output_idx_type: An optional `tf.DType` from: `tf.int32, tf.int64`. Defaults to `tf.int32`.
    name: A name for the operation (optional).

  Returns:
    A tuple of `Tensor` objects (lu, p).

    lu: A `Tensor`. Has the same type as `input`.
    p: A `Tensor` of type `output_idx_type`.
  """
  _ctx = _context._context or _context.context()
  tld = _ctx._thread_local_data
  if tld.is_eager:
    try:
      _result = pywrap_tfe.TFE_Py_FastPathExecute(
        _ctx._context_handle, tld.device_name, "Lu", name, tld.op_callbacks,
        input, "output_idx_type", output_idx_type)
      _result = _LuOutput._make(_result)
      return _result
    except _core._FallbackException:
      try:
        return lu_eager_fallback(
            input, output_idx_type=output_idx_type, name=name, ctx=_ctx)
      except _core._SymbolicException:
        pass  # Add nodes to the TensorFlow graph.
      except (TypeError, ValueError):
        result = _dispatch.dispatch(
              lu, input=input, output_idx_type=output_idx_type, name=name)
        if result is not _dispatch.OpDispatcher.NOT_SUPPORTED:
          return result
        raise
    except _core._NotOkStatusException as e:
      _ops.raise_from_not_ok_status(e, name)
  # Add nodes to the TensorFlow graph.
  if output_idx_type is None:
    output_idx_type = _dtypes.int32
  output_idx_type = _execute.make_type(output_idx_type, "output_idx_type")
  try:
    _, _, _op, _outputs = _op_def_library._apply_op_helper(
        "Lu", input=input, output_idx_type=output_idx_type, name=name)
  except (TypeError, ValueError):
    result = _dispatch.dispatch(
          lu, input=input, output_idx_type=output_idx_type, name=name)
    if result is not _dispatch.OpDispatcher.NOT_SUPPORTED:
      return result
    raise
  _result = _outputs[:]
  if _execute.must_record_gradient():
    _attrs = ("T", _op._get_attr_type("T"), "output_idx_type",
              _op._get_attr_type("output_idx_type"))
    _inputs_flat = _op.inputs
    _execute.record_gradient(
        "Lu", _inputs_flat, _attrs, _result)
  _result = _LuOutput._make(_result)
  return _result

Lu = tf_export("raw_ops.Lu")(_ops.to_raw_op(lu))


def lu_eager_fallback(input, output_idx_type, name, ctx):
  if output_idx_type is None:
    output_idx_type = _dtypes.int32
  output_idx_type = _execute.make_type(output_idx_type, "output_idx_type")
  _attr_T, (input,) = _execute.args_to_matching_eager([input], ctx)
  _inputs_flat = [input]
  _attrs = ("T", _attr_T, "output_idx_type", output_idx_type)
  _result = _execute.execute(b"Lu", 2, inputs=_inputs_flat, attrs=_attrs,
                             ctx=ctx, name=name)
  if _execute.must_record_gradient():
    _execute.record_gradient(
        "Lu", _inputs_flat, _attrs, _result)
  _result = _LuOutput._make(_result)
  return _result


@_dispatch.add_dispatch_list
@tf_export('linalg.det', v1=['linalg.det', 'matrix_determinant'])
@deprecated_endpoints('matrix_determinant')
def matrix_determinant(input, name=None):
  r"""Computes the determinant of one or more square matrices.

  The input is a tensor of shape `[..., M, M]` whose inner-most 2 dimensions
  form square matrices. The output is a tensor containing the determinants
  for all input submatrices `[..., :, :]`.

  Args:
    input: A `Tensor`. Must be one of the following types: `half`, `float32`, `float64`, `complex64`, `complex128`.
      Shape is `[..., M, M]`.
    name: A name for the operation (optional).

  Returns:
    A `Tensor`. Has the same type as `input`.
  """
  _ctx = _context._context or _context.context()
  tld = _ctx._thread_local_data
  if tld.is_eager:
    try:
      _result = pywrap_tfe.TFE_Py_FastPathExecute(
        _ctx._context_handle, tld.device_name, "MatrixDeterminant", name,
        tld.op_callbacks, input)
      return _result
    except _core._FallbackException:
      try:
        return matrix_determinant_eager_fallback(
            input, name=name, ctx=_ctx)
      except _core._SymbolicException:
        pass  # Add nodes to the TensorFlow graph.
      except (TypeError, ValueError):
        result = _dispatch.dispatch(
              matrix_determinant, input=input, name=name)
        if result is not _dispatch.OpDispatcher.NOT_SUPPORTED:
          return result
        raise
    except _core._NotOkStatusException as e:
      _ops.raise_from_not_ok_status(e, name)
  # Add nodes to the TensorFlow graph.
  try:
    _, _, _op, _outputs = _op_def_library._apply_op_helper(
        "MatrixDeterminant", input=input, name=name)
  except (TypeError, ValueError):
    result = _dispatch.dispatch(
          matrix_determinant, input=input, name=name)
    if result is not _dispatch.OpDispatcher.NOT_SUPPORTED:
      return result
    raise
  _result = _outputs[:]
  if _execute.must_record_gradient():
    _attrs = ("T", _op._get_attr_type("T"))
    _inputs_flat = _op.inputs
    _execute.record_gradient(
        "MatrixDeterminant", _inputs_flat, _attrs, _result)
  _result, = _result
  return _result

MatrixDeterminant = tf_export("raw_ops.MatrixDeterminant")(_ops.to_raw_op(matrix_determinant))


def matrix_determinant_eager_fallback(input, name, ctx):
  _attr_T, (input,) = _execute.args_to_matching_eager([input], ctx)
  _inputs_flat = [input]
  _attrs = ("T", _attr_T)
  _result = _execute.execute(b"MatrixDeterminant", 1, inputs=_inputs_flat,
                             attrs=_attrs, ctx=ctx, name=name)
  if _execute.must_record_gradient():
    _execute.record_gradient(
        "MatrixDeterminant", _inputs_flat, _attrs, _result)
  _result, = _result
  return _result


def matrix_exponential(input, name=None):
  r"""Deprecated, use python implementation tf.linalg.matrix_exponential.

  Args:
    input: A `Tensor`. Must be one of the following types: `float64`, `float32`, `half`, `complex64`, `complex128`.
    name: A name for the operation (optional).

  Returns:
    A `Tensor`. Has the same type as `input`.
  """
  _ctx = _context._context or _context.context()
  tld = _ctx._thread_local_data
  if tld.is_eager:
    try:
      _result = pywrap_tfe.TFE_Py_FastPathExecute(
        _ctx._context_handle, tld.device_name, "MatrixExponential", name,
        tld.op_callbacks, input)
      return _result
    except _core._FallbackException:
      try:
        return matrix_exponential_eager_fallback(
            input, name=name, ctx=_ctx)
      except _core._SymbolicException:
        pass  # Add nodes to the TensorFlow graph.
    except _core._NotOkStatusException as e:
      _ops.raise_from_not_ok_status(e, name)
  # Add nodes to the TensorFlow graph.
  _, _, _op, _outputs = _op_def_library._apply_op_helper(
        "MatrixExponential", input=input, name=name)
  _result = _outputs[:]
  if _execute.must_record_gradient():
    _attrs = ("T", _op._get_attr_type("T"))
    _inputs_flat = _op.inputs
    _execute.record_gradient(
        "MatrixExponential", _inputs_flat, _attrs, _result)
  _result, = _result
  return _result

MatrixExponential = tf_export("raw_ops.MatrixExponential")(_ops.to_raw_op(matrix_exponential))


def matrix_exponential_eager_fallback(input, name, ctx):
  _attr_T, (input,) = _execute.args_to_matching_eager([input], ctx)
  _inputs_flat = [input]
  _attrs = ("T", _attr_T)
  _result = _execute.execute(b"MatrixExponential", 1, inputs=_inputs_flat,
                             attrs=_attrs, ctx=ctx, name=name)
  if _execute.must_record_gradient():
    _execute.record_gradient(
        "MatrixExponential", _inputs_flat, _attrs, _result)
  _result, = _result
  return _result


@_dispatch.add_dispatch_list
@tf_export('linalg.inv', v1=['linalg.inv', 'matrix_inverse'])
@deprecated_endpoints('matrix_inverse')
def matrix_inverse(input, adjoint=False, name=None):
  r"""Computes the inverse of one or more square invertible matrices or their

  adjoints (conjugate transposes).

  The input is a tensor of shape `[..., M, M]` whose inner-most 2 dimensions
  form square matrices. The output is a tensor of the same shape as the input
  containing the inverse for all input submatrices `[..., :, :]`.

  The op uses LU decomposition with partial pivoting to compute the inverses.

  If a matrix is not invertible there is no guarantee what the op does. It
  may detect the condition and raise an exception or it may simply return a
  garbage result.

  Args:
    input: A `Tensor`. Must be one of the following types: `float64`, `float32`, `half`, `complex64`, `complex128`.
      Shape is `[..., M, M]`.
    adjoint: An optional `bool`. Defaults to `False`.
    name: A name for the operation (optional).

  Returns:
    A `Tensor`. Has the same type as `input`.
  """
  _ctx = _context._context or _context.context()
  tld = _ctx._thread_local_data
  if tld.is_eager:
    try:
      _result = pywrap_tfe.TFE_Py_FastPathExecute(
        _ctx._context_handle, tld.device_name, "MatrixInverse", name,
        tld.op_callbacks, input, "adjoint", adjoint)
      return _result
    except _core._FallbackException:
      try:
        return matrix_inverse_eager_fallback(
            input, adjoint=adjoint, name=name, ctx=_ctx)
      except _core._SymbolicException:
        pass  # Add nodes to the TensorFlow graph.
      except (TypeError, ValueError):
        result = _dispatch.dispatch(
              matrix_inverse, input=input, adjoint=adjoint, name=name)
        if result is not _dispatch.OpDispatcher.NOT_SUPPORTED:
          return result
        raise
    except _core._NotOkStatusException as e:
      _ops.raise_from_not_ok_status(e, name)
  # Add nodes to the TensorFlow graph.
  if adjoint is None:
    adjoint = False
  adjoint = _execute.make_bool(adjoint, "adjoint")
  try:
    _, _, _op, _outputs = _op_def_library._apply_op_helper(
        "MatrixInverse", input=input, adjoint=adjoint, name=name)
  except (TypeError, ValueError):
    result = _dispatch.dispatch(
          matrix_inverse, input=input, adjoint=adjoint, name=name)
    if result is not _dispatch.OpDispatcher.NOT_SUPPORTED:
      return result
    raise
  _result = _outputs[:]
  if _execute.must_record_gradient():
    _attrs = ("adjoint", _op._get_attr_bool("adjoint"), "T",
              _op._get_attr_type("T"))
    _inputs_flat = _op.inputs
    _execute.record_gradient(
        "MatrixInverse", _inputs_flat, _attrs, _result)
  _result, = _result
  return _result

MatrixInverse = tf_export("raw_ops.MatrixInverse")(_ops.to_raw_op(matrix_inverse))


def matrix_inverse_eager_fallback(input, adjoint, name, ctx):
  if adjoint is None:
    adjoint = False
  adjoint = _execute.make_bool(adjoint, "adjoint")
  _attr_T, (input,) = _execute.args_to_matching_eager([input], ctx)
  _inputs_flat = [input]
  _attrs = ("adjoint", adjoint, "T", _attr_T)
  _result = _execute.execute(b"MatrixInverse", 1, inputs=_inputs_flat,
                             attrs=_attrs, ctx=ctx, name=name)
  if _execute.must_record_gradient():
    _execute.record_gradient(
        "MatrixInverse", _inputs_flat, _attrs, _result)
  _result, = _result
  return _result


def matrix_logarithm(input, name=None):
  r"""Computes the matrix logarithm of one or more square matrices:

  
  \\(log(exp(A)) = A\\)

  This op is only defined for complex matrices. If A is positive-definite and
  real, then casting to a complex matrix, taking the logarithm and casting back
  to a real matrix will give the correct result.

  This function computes the matrix logarithm using the Schur-Parlett algorithm.
  Details of the algorithm can be found in Section 11.6.2 of:
  Nicholas J. Higham, Functions of Matrices: Theory and Computation, SIAM 2008.
  ISBN 978-0-898716-46-7.

  The input is a tensor of shape `[..., M, M]` whose inner-most 2 dimensions
  form square matrices. The output is a tensor of the same shape as the input
  containing the exponential for all input submatrices `[..., :, :]`.

  Args:
    input: A `Tensor`. Must be one of the following types: `complex64`, `complex128`.
      Shape is `[..., M, M]`.
    name: A name for the operation (optional).

  Returns:
    A `Tensor`. Has the same type as `input`.
  """
  _ctx = _context._context or _context.context()
  tld = _ctx._thread_local_data
  if tld.is_eager:
    try:
      _result = pywrap_tfe.TFE_Py_FastPathExecute(
        _ctx._context_handle, tld.device_name, "MatrixLogarithm", name,
        tld.op_callbacks, input)
      return _result
    except _core._FallbackException:
      try:
        return matrix_logarithm_eager_fallback(
            input, name=name, ctx=_ctx)
      except _core._SymbolicException:
        pass  # Add nodes to the TensorFlow graph.
    except _core._NotOkStatusException as e:
      _ops.raise_from_not_ok_status(e, name)
  # Add nodes to the TensorFlow graph.
  _, _, _op, _outputs = _op_def_library._apply_op_helper(
        "MatrixLogarithm", input=input, name=name)
  _result = _outputs[:]
  if _execute.must_record_gradient():
    _attrs = ("T", _op._get_attr_type("T"))
    _inputs_flat = _op.inputs
    _execute.record_gradient(
        "MatrixLogarithm", _inputs_flat, _attrs, _result)
  _result, = _result
  return _result

MatrixLogarithm = tf_export("raw_ops.MatrixLogarithm")(_ops.to_raw_op(matrix_logarithm))


def matrix_logarithm_eager_fallback(input, name, ctx):
  _attr_T, (input,) = _execute.args_to_matching_eager([input], ctx)
  _inputs_flat = [input]
  _attrs = ("T", _attr_T)
  _result = _execute.execute(b"MatrixLogarithm", 1, inputs=_inputs_flat,
                             attrs=_attrs, ctx=ctx, name=name)
  if _execute.must_record_gradient():
    _execute.record_gradient(
        "MatrixLogarithm", _inputs_flat, _attrs, _result)
  _result, = _result
  return _result


@_dispatch.add_dispatch_list
@tf_export('linalg.solve', v1=['linalg.solve', 'matrix_solve'])
@deprecated_endpoints('matrix_solve')
def matrix_solve(matrix, rhs, adjoint=False, name=None):
  r"""Solves systems of linear equations.

  `Matrix` is a tensor of shape `[..., M, M]` whose inner-most 2 dimensions
  form square matrices. `Rhs` is a tensor of shape `[..., M, K]`. The `output` is
  a tensor shape `[..., M, K]`.  If `adjoint` is `False` then each output matrix
  satisfies `matrix[..., :, :] * output[..., :, :] = rhs[..., :, :]`.
  If `adjoint` is `True` then each output matrix satisfies
  `adjoint(matrix[..., :, :]) * output[..., :, :] = rhs[..., :, :]`.

  Args:
    matrix: A `Tensor`. Must be one of the following types: `float64`, `float32`, `half`, `complex64`, `complex128`.
      Shape is `[..., M, M]`.
    rhs: A `Tensor`. Must have the same type as `matrix`.
      Shape is `[..., M, K]`.
    adjoint: An optional `bool`. Defaults to `False`.
      Boolean indicating whether to solve with `matrix` or its (block-wise)
      adjoint.
    name: A name for the operation (optional).

  Returns:
    A `Tensor`. Has the same type as `matrix`.
  """
  _ctx = _context._context or _context.context()
  tld = _ctx._thread_local_data
  if tld.is_eager:
    try:
      _result = pywrap_tfe.TFE_Py_FastPathExecute(
        _ctx._context_handle, tld.device_name, "MatrixSolve", name,
        tld.op_callbacks, matrix, rhs, "adjoint", adjoint)
      return _result
    except _core._FallbackException:
      try:
        return matrix_solve_eager_fallback(
            matrix, rhs, adjoint=adjoint, name=name, ctx=_ctx)
      except _core._SymbolicException:
        pass  # Add nodes to the TensorFlow graph.
      except (TypeError, ValueError):
        result = _dispatch.dispatch(
              matrix_solve, matrix=matrix, rhs=rhs, adjoint=adjoint,
                            name=name)
        if result is not _dispatch.OpDispatcher.NOT_SUPPORTED:
          return result
        raise
    except _core._NotOkStatusException as e:
      _ops.raise_from_not_ok_status(e, name)
  # Add nodes to the TensorFlow graph.
  if adjoint is None:
    adjoint = False
  adjoint = _execute.make_bool(adjoint, "adjoint")
  try:
    _, _, _op, _outputs = _op_def_library._apply_op_helper(
        "MatrixSolve", matrix=matrix, rhs=rhs, adjoint=adjoint, name=name)
  except (TypeError, ValueError):
    result = _dispatch.dispatch(
          matrix_solve, matrix=matrix, rhs=rhs, adjoint=adjoint, name=name)
    if result is not _dispatch.OpDispatcher.NOT_SUPPORTED:
      return result
    raise
  _result = _outputs[:]
  if _execute.must_record_gradient():
    _attrs = ("adjoint", _op._get_attr_bool("adjoint"), "T",
              _op._get_attr_type("T"))
    _inputs_flat = _op.inputs
    _execute.record_gradient(
        "MatrixSolve", _inputs_flat, _attrs, _result)
  _result, = _result
  return _result

MatrixSolve = tf_export("raw_ops.MatrixSolve")(_ops.to_raw_op(matrix_solve))


def matrix_solve_eager_fallback(matrix, rhs, adjoint, name, ctx):
  if adjoint is None:
    adjoint = False
  adjoint = _execute.make_bool(adjoint, "adjoint")
  _attr_T, _inputs_T = _execute.args_to_matching_eager([matrix, rhs], ctx)
  (matrix, rhs) = _inputs_T
  _inputs_flat = [matrix, rhs]
  _attrs = ("adjoint", adjoint, "T", _attr_T)
  _result = _execute.execute(b"MatrixSolve", 1, inputs=_inputs_flat,
                             attrs=_attrs, ctx=ctx, name=name)
  if _execute.must_record_gradient():
    _execute.record_gradient(
        "MatrixSolve", _inputs_flat, _attrs, _result)
  _result, = _result
  return _result


def matrix_solve_ls(matrix, rhs, l2_regularizer, fast=True, name=None):
  r"""Solves one or more linear least-squares problems.

  `matrix` is a tensor of shape `[..., M, N]` whose inner-most 2 dimensions
  form real or complex matrices of size `[M, N]`. `Rhs` is a tensor of the same
  type as `matrix` and shape `[..., M, K]`.
  The output is a tensor shape `[..., N, K]` where each output matrix solves
  each of the equations
  `matrix[..., :, :]` * `output[..., :, :]` = `rhs[..., :, :]`
  in the least squares sense.

  We use the following notation for (complex) matrix and right-hand sides
  in the batch:

  `matrix`=\\(A \in \mathbb{C}^{m \times n}\\),
  `rhs`=\\(B  \in \mathbb{C}^{m \times k}\\),
  `output`=\\(X  \in \mathbb{C}^{n \times k}\\),
  `l2_regularizer`=\\(\lambda \in \mathbb{R}\\).

  If `fast` is `True`, then the solution is computed by solving the normal
  equations using Cholesky decomposition. Specifically, if \\(m \ge n\\) then
  \\(X = (A^H A + \lambda I)^{-1} A^H B\\), which solves the least-squares
  problem \\(X = \mathrm{argmin}_{Z \in \Re^{n \times k} } ||A Z - B||_F^2 + \lambda ||Z||_F^2\\).
  If \\(m \lt n\\) then `output` is computed as
  \\(X = A^H (A A^H + \lambda I)^{-1} B\\), which (for \\(\lambda = 0\\)) is the
  minimum-norm solution to the under-determined linear system, i.e.
  \\(X = \mathrm{argmin}_{Z \in \mathbb{C}^{n \times k} } ||Z||_F^2 \\),
  subject to \\(A Z = B\\). Notice that the fast path is only numerically stable
  when \\(A\\) is numerically full rank and has a condition number
  \\(\mathrm{cond}(A) \lt \frac{1}{\sqrt{\epsilon_{mach} } }\\) or \\(\lambda\\) is
  sufficiently large.

  If `fast` is `False` an algorithm based on the numerically robust complete
  orthogonal decomposition is used. This computes the minimum-norm
  least-squares solution, even when \\(A\\) is rank deficient. This path is
  typically 6-7 times slower than the fast path. If `fast` is `False` then
  `l2_regularizer` is ignored.

  Args:
    matrix: A `Tensor`. Must be one of the following types: `float64`, `float32`, `half`, `complex64`, `complex128`.
      Shape is `[..., M, N]`.
    rhs: A `Tensor`. Must have the same type as `matrix`.
      Shape is `[..., M, K]`.
    l2_regularizer: A `Tensor` of type `float64`. Scalar tensor.

      @compatibility(numpy)
      Equivalent to np.linalg.lstsq
      @end_compatibility
    fast: An optional `bool`. Defaults to `True`.
    name: A name for the operation (optional).

  Returns:
    A `Tensor`. Has the same type as `matrix`.
  """
  _ctx = _context._context or _context.context()
  tld = _ctx._thread_local_data
  if tld.is_eager:
    try:
      _result = pywrap_tfe.TFE_Py_FastPathExecute(
        _ctx._context_handle, tld.device_name, "MatrixSolveLs", name,
        tld.op_callbacks, matrix, rhs, l2_regularizer, "fast", fast)
      return _result
    except _core._FallbackException:
      try:
        return matrix_solve_ls_eager_fallback(
            matrix, rhs, l2_regularizer, fast=fast, name=name, ctx=_ctx)
      except _core._SymbolicException:
        pass  # Add nodes to the TensorFlow graph.
    except _core._NotOkStatusException as e:
      _ops.raise_from_not_ok_status(e, name)
  # Add nodes to the TensorFlow graph.
  if fast is None:
    fast = True
  fast = _execute.make_bool(fast, "fast")
  _, _, _op, _outputs = _op_def_library._apply_op_helper(
        "MatrixSolveLs", matrix=matrix, rhs=rhs,
                         l2_regularizer=l2_regularizer, fast=fast, name=name)
  _result = _outputs[:]
  if _execute.must_record_gradient():
    _attrs = ("T", _op._get_attr_type("T"), "fast",
              _op._get_attr_bool("fast"))
    _inputs_flat = _op.inputs
    _execute.record_gradient(
        "MatrixSolveLs", _inputs_flat, _attrs, _result)
  _result, = _result
  return _result

MatrixSolveLs = tf_export("raw_ops.MatrixSolveLs")(_ops.to_raw_op(matrix_solve_ls))


def matrix_solve_ls_eager_fallback(matrix, rhs, l2_regularizer, fast, name, ctx):
  if fast is None:
    fast = True
  fast = _execute.make_bool(fast, "fast")
  _attr_T, _inputs_T = _execute.args_to_matching_eager([matrix, rhs], ctx)
  (matrix, rhs) = _inputs_T
  l2_regularizer = _ops.convert_to_tensor(l2_regularizer, _dtypes.float64)
  _inputs_flat = [matrix, rhs, l2_regularizer]
  _attrs = ("T", _attr_T, "fast", fast)
  _result = _execute.execute(b"MatrixSolveLs", 1, inputs=_inputs_flat,
                             attrs=_attrs, ctx=ctx, name=name)
  if _execute.must_record_gradient():
    _execute.record_gradient(
        "MatrixSolveLs", _inputs_flat, _attrs, _result)
  _result, = _result
  return _result


@_dispatch.add_dispatch_list
@tf_export('linalg.sqrtm', 'matrix_square_root')
def matrix_square_root(input, name=None):
  r"""Computes the matrix square root of one or more square matrices:

  matmul(sqrtm(A), sqrtm(A)) = A

  The input matrix should be invertible. If the input matrix is real, it should
  have no eigenvalues which are real and negative (pairs of complex conjugate
  eigenvalues are allowed).

  The matrix square root is computed by first reducing the matrix to
  quasi-triangular form with the real Schur decomposition. The square root
  of the quasi-triangular matrix is then computed directly. Details of
  the algorithm can be found in: Nicholas J. Higham, "Computing real
  square roots of a real matrix", Linear Algebra Appl., 1987.

  The input is a tensor of shape `[..., M, M]` whose inner-most 2 dimensions
  form square matrices. The output is a tensor of the same shape as the input
  containing the matrix square root for all input submatrices `[..., :, :]`.

  Args:
    input: A `Tensor`. Must be one of the following types: `float64`, `float32`, `half`, `complex64`, `complex128`.
      Shape is `[..., M, M]`.
    name: A name for the operation (optional).

  Returns:
    A `Tensor`. Has the same type as `input`.
  """
  _ctx = _context._context or _context.context()
  tld = _ctx._thread_local_data
  if tld.is_eager:
    try:
      _result = pywrap_tfe.TFE_Py_FastPathExecute(
        _ctx._context_handle, tld.device_name, "MatrixSquareRoot", name,
        tld.op_callbacks, input)
      return _result
    except _core._FallbackException:
      try:
        return matrix_square_root_eager_fallback(
            input, name=name, ctx=_ctx)
      except _core._SymbolicException:
        pass  # Add nodes to the TensorFlow graph.
      except (TypeError, ValueError):
        result = _dispatch.dispatch(
              matrix_square_root, input=input, name=name)
        if result is not _dispatch.OpDispatcher.NOT_SUPPORTED:
          return result
        raise
    except _core._NotOkStatusException as e:
      _ops.raise_from_not_ok_status(e, name)
  # Add nodes to the TensorFlow graph.
  try:
    _, _, _op, _outputs = _op_def_library._apply_op_helper(
        "MatrixSquareRoot", input=input, name=name)
  except (TypeError, ValueError):
    result = _dispatch.dispatch(
          matrix_square_root, input=input, name=name)
    if result is not _dispatch.OpDispatcher.NOT_SUPPORTED:
      return result
    raise
  _result = _outputs[:]
  if _execute.must_record_gradient():
    _attrs = ("T", _op._get_attr_type("T"))
    _inputs_flat = _op.inputs
    _execute.record_gradient(
        "MatrixSquareRoot", _inputs_flat, _attrs, _result)
  _result, = _result
  return _result

MatrixSquareRoot = tf_export("raw_ops.MatrixSquareRoot")(_ops.to_raw_op(matrix_square_root))


def matrix_square_root_eager_fallback(input, name, ctx):
  _attr_T, (input,) = _execute.args_to_matching_eager([input], ctx)
  _inputs_flat = [input]
  _attrs = ("T", _attr_T)
  _result = _execute.execute(b"MatrixSquareRoot", 1, inputs=_inputs_flat,
                             attrs=_attrs, ctx=ctx, name=name)
  if _execute.must_record_gradient():
    _execute.record_gradient(
        "MatrixSquareRoot", _inputs_flat, _attrs, _result)
  _result, = _result
  return _result


def matrix_triangular_solve(matrix, rhs, lower=True, adjoint=False, name=None):
  r"""Solves systems of linear equations with upper or lower triangular matrices by backsubstitution.

  
  `matrix` is a tensor of shape `[..., M, M]` whose inner-most 2 dimensions form
  square matrices. If `lower` is `True` then the strictly upper triangular part
  of each inner-most matrix is assumed to be zero and not accessed.
  If `lower` is False then the strictly lower triangular part of each inner-most
  matrix is assumed to be zero and not accessed.
  `rhs` is a tensor of shape `[..., M, N]`.

  The output is a tensor of shape `[..., M, N]`. If `adjoint` is
  `True` then the innermost matrices in `output` satisfy matrix equations
  `matrix[..., :, :] * output[..., :, :] = rhs[..., :, :]`.
  If `adjoint` is `False` then the strictly then the  innermost matrices in
  `output` satisfy matrix equations
  `adjoint(matrix[..., i, k]) * output[..., k, j] = rhs[..., i, j]`.

  Note, the batch shapes for the inputs only need to broadcast.

  Example:
  ```python

  a = tf.constant([[3,  0,  0,  0],
                   [2,  1,  0,  0],
                   [1,  0,  1,  0],
                   [1,  1,  1,  1]], dtype=tf.float32)

  b = tf.constant([[4],
                   [2],
                   [4],
                   [2]], dtype=tf.float32)

  x = tf.linalg.triangular_solve(a, b, lower=True)
  x
  # <tf.Tensor: shape=(4, 1), dtype=float32, numpy=
  # array([[ 1.3333334 ],
  #        [-0.66666675],
  #        [ 2.6666665 ],
  #        [-1.3333331 ]], dtype=float32)>

  # in python3 one can use `a@x`
  tf.matmul(a, x)
  # <tf.Tensor: shape=(4, 1), dtype=float32, numpy=
  # array([[4.       ],
  #        [2.       ],
  #        [4.       ],
  #        [1.9999999]], dtype=float32)>
  ```

  Args:
    matrix: A `Tensor`. Must be one of the following types: `float64`, `float32`, `half`, `complex64`, `complex128`.
      Shape is `[..., M, M]`.
    rhs: A `Tensor`. Must have the same type as `matrix`.
      Shape is `[..., M, K]`.
    lower: An optional `bool`. Defaults to `True`.
      Boolean indicating whether the innermost matrices in `matrix` are
      lower or upper triangular.
    adjoint: An optional `bool`. Defaults to `False`.
      Boolean indicating whether to solve with `matrix` or its (block-wise)
               adjoint.

      @compatibility(numpy)
      Equivalent to scipy.linalg.solve_triangular
      @end_compatibility
    name: A name for the operation (optional).

  Returns:
    A `Tensor`. Has the same type as `matrix`.
  """
  _ctx = _context._context or _context.context()
  tld = _ctx._thread_local_data
  if tld.is_eager:
    try:
      _result = pywrap_tfe.TFE_Py_FastPathExecute(
        _ctx._context_handle, tld.device_name, "MatrixTriangularSolve", name,
        tld.op_callbacks, matrix, rhs, "lower", lower, "adjoint", adjoint)
      return _result
    except _core._FallbackException:
      try:
        return matrix_triangular_solve_eager_fallback(
            matrix, rhs, lower=lower, adjoint=adjoint, name=name, ctx=_ctx)
      except _core._SymbolicException:
        pass  # Add nodes to the TensorFlow graph.
    except _core._NotOkStatusException as e:
      _ops.raise_from_not_ok_status(e, name)
  # Add nodes to the TensorFlow graph.
  if lower is None:
    lower = True
  lower = _execute.make_bool(lower, "lower")
  if adjoint is None:
    adjoint = False
  adjoint = _execute.make_bool(adjoint, "adjoint")
  _, _, _op, _outputs = _op_def_library._apply_op_helper(
        "MatrixTriangularSolve", matrix=matrix, rhs=rhs, lower=lower,
                                 adjoint=adjoint, name=name)
  _result = _outputs[:]
  if _execute.must_record_gradient():
    _attrs = ("lower", _op._get_attr_bool("lower"), "adjoint",
              _op._get_attr_bool("adjoint"), "T", _op._get_attr_type("T"))
    _inputs_flat = _op.inputs
    _execute.record_gradient(
        "MatrixTriangularSolve", _inputs_flat, _attrs, _result)
  _result, = _result
  return _result

MatrixTriangularSolve = tf_export("raw_ops.MatrixTriangularSolve")(_ops.to_raw_op(matrix_triangular_solve))


def matrix_triangular_solve_eager_fallback(matrix, rhs, lower, adjoint, name, ctx):
  if lower is None:
    lower = True
  lower = _execute.make_bool(lower, "lower")
  if adjoint is None:
    adjoint = False
  adjoint = _execute.make_bool(adjoint, "adjoint")
  _attr_T, _inputs_T = _execute.args_to_matching_eager([matrix, rhs], ctx)
  (matrix, rhs) = _inputs_T
  _inputs_flat = [matrix, rhs]
  _attrs = ("lower", lower, "adjoint", adjoint, "T", _attr_T)
  _result = _execute.execute(b"MatrixTriangularSolve", 1, inputs=_inputs_flat,
                             attrs=_attrs, ctx=ctx, name=name)
  if _execute.must_record_gradient():
    _execute.record_gradient(
        "MatrixTriangularSolve", _inputs_flat, _attrs, _result)
  _result, = _result
  return _result

_QrOutput = collections.namedtuple(
    "Qr",
    ["q", "r"])


@_dispatch.add_dispatch_list
@tf_export('linalg.qr', v1=['linalg.qr', 'qr'])
@deprecated_endpoints('qr')
def qr(input, full_matrices=False, name=None):
  r"""Computes the QR decompositions of one or more matrices.

  Computes the QR decomposition of each inner matrix in `tensor` such that
  `tensor[..., :, :] = q[..., :, :] * r[..., :,:])`

  ```python
  # a is a tensor.
  # q is a tensor of orthonormal matrices.
  # r is a tensor of upper triangular matrices.
  q, r = qr(a)
  q_full, r_full = qr(a, full_matrices=True)
  ```

  Args:
    input: A `Tensor`. Must be one of the following types: `float64`, `float32`, `half`, `complex64`, `complex128`.
      A tensor of shape `[..., M, N]` whose inner-most 2 dimensions
      form matrices of size `[M, N]`. Let `P` be the minimum of `M` and `N`.
    full_matrices: An optional `bool`. Defaults to `False`.
      If true, compute full-sized `q` and `r`. If false
      (the default), compute only the leading `P` columns of `q`.
    name: A name for the operation (optional).

  Returns:
    A tuple of `Tensor` objects (q, r).

    q: A `Tensor`. Has the same type as `input`.
    r: A `Tensor`. Has the same type as `input`.
  """
  _ctx = _context._context or _context.context()
  tld = _ctx._thread_local_data
  if tld.is_eager:
    try:
      _result = pywrap_tfe.TFE_Py_FastPathExecute(
        _ctx._context_handle, tld.device_name, "Qr", name, tld.op_callbacks,
        input, "full_matrices", full_matrices)
      _result = _QrOutput._make(_result)
      return _result
    except _core._FallbackException:
      try:
        return qr_eager_fallback(
            input, full_matrices=full_matrices, name=name, ctx=_ctx)
      except _core._SymbolicException:
        pass  # Add nodes to the TensorFlow graph.
      except (TypeError, ValueError):
        result = _dispatch.dispatch(
              qr, input=input, full_matrices=full_matrices, name=name)
        if result is not _dispatch.OpDispatcher.NOT_SUPPORTED:
          return result
        raise
    except _core._NotOkStatusException as e:
      _ops.raise_from_not_ok_status(e, name)
  # Add nodes to the TensorFlow graph.
  if full_matrices is None:
    full_matrices = False
  full_matrices = _execute.make_bool(full_matrices, "full_matrices")
  try:
    _, _, _op, _outputs = _op_def_library._apply_op_helper(
        "Qr", input=input, full_matrices=full_matrices, name=name)
  except (TypeError, ValueError):
    result = _dispatch.dispatch(
          qr, input=input, full_matrices=full_matrices, name=name)
    if result is not _dispatch.OpDispatcher.NOT_SUPPORTED:
      return result
    raise
  _result = _outputs[:]
  if _execute.must_record_gradient():
    _attrs = ("full_matrices", _op._get_attr_bool("full_matrices"), "T",
              _op._get_attr_type("T"))
    _inputs_flat = _op.inputs
    _execute.record_gradient(
        "Qr", _inputs_flat, _attrs, _result)
  _result = _QrOutput._make(_result)
  return _result

Qr = tf_export("raw_ops.Qr")(_ops.to_raw_op(qr))


def qr_eager_fallback(input, full_matrices, name, ctx):
  if full_matrices is None:
    full_matrices = False
  full_matrices = _execute.make_bool(full_matrices, "full_matrices")
  _attr_T, (input,) = _execute.args_to_matching_eager([input], ctx)
  _inputs_flat = [input]
  _attrs = ("full_matrices", full_matrices, "T", _attr_T)
  _result = _execute.execute(b"Qr", 2, inputs=_inputs_flat, attrs=_attrs,
                             ctx=ctx, name=name)
  if _execute.must_record_gradient():
    _execute.record_gradient(
        "Qr", _inputs_flat, _attrs, _result)
  _result = _QrOutput._make(_result)
  return _result


def self_adjoint_eig(input, name=None):
  r"""Computes the Eigen Decomposition of a batch of square self-adjoint matrices.

  The input is a tensor of shape `[..., M, M]` whose inner-most 2 dimensions
  form square matrices, with the same constraints as the single matrix
  SelfAdjointEig.

  The result is a [..., M+1, M] matrix with [..., 0,:] containing the
  eigenvalues, and subsequent [...,1:, :] containing the eigenvectors. The eigenvalues
  are sorted in non-decreasing order.

  Args:
    input: A `Tensor`. Must be one of the following types: `float64`, `float32`, `half`.
      Shape is `[..., M, M]`.
    name: A name for the operation (optional).

  Returns:
    A `Tensor`. Has the same type as `input`.
  """
  _ctx = _context._context or _context.context()
  tld = _ctx._thread_local_data
  if tld.is_eager:
    try:
      _result = pywrap_tfe.TFE_Py_FastPathExecute(
        _ctx._context_handle, tld.device_name, "SelfAdjointEig", name,
        tld.op_callbacks, input)
      return _result
    except _core._FallbackException:
      try:
        return self_adjoint_eig_eager_fallback(
            input, name=name, ctx=_ctx)
      except _core._SymbolicException:
        pass  # Add nodes to the TensorFlow graph.
    except _core._NotOkStatusException as e:
      _ops.raise_from_not_ok_status(e, name)
  # Add nodes to the TensorFlow graph.
  _, _, _op, _outputs = _op_def_library._apply_op_helper(
        "SelfAdjointEig", input=input, name=name)
  _result = _outputs[:]
  if _execute.must_record_gradient():
    _attrs = ("T", _op._get_attr_type("T"))
    _inputs_flat = _op.inputs
    _execute.record_gradient(
        "SelfAdjointEig", _inputs_flat, _attrs, _result)
  _result, = _result
  return _result

SelfAdjointEig = tf_export("raw_ops.SelfAdjointEig")(_ops.to_raw_op(self_adjoint_eig))


def self_adjoint_eig_eager_fallback(input, name, ctx):
  _attr_T, (input,) = _execute.args_to_matching_eager([input], ctx)
  _inputs_flat = [input]
  _attrs = ("T", _attr_T)
  _result = _execute.execute(b"SelfAdjointEig", 1, inputs=_inputs_flat,
                             attrs=_attrs, ctx=ctx, name=name)
  if _execute.must_record_gradient():
    _execute.record_gradient(
        "SelfAdjointEig", _inputs_flat, _attrs, _result)
  _result, = _result
  return _result

_SelfAdjointEigV2Output = collections.namedtuple(
    "SelfAdjointEigV2",
    ["e", "v"])


def self_adjoint_eig_v2(input, compute_v=True, name=None):
  r"""Computes the eigen decomposition of one or more square self-adjoint matrices.

  Computes the eigenvalues and (optionally) eigenvectors of each inner matrix in
  `input` such that `input[..., :, :] = v[..., :, :] * diag(e[..., :])`. The eigenvalues
  are sorted in non-decreasing order.

  ```python
  # a is a tensor.
  # e is a tensor of eigenvalues.
  # v is a tensor of eigenvectors.
  e, v = self_adjoint_eig(a)
  e = self_adjoint_eig(a, compute_v=False)
  ```

  Args:
    input: A `Tensor`. Must be one of the following types: `float64`, `float32`, `half`, `complex64`, `complex128`.
      `Tensor` input of shape `[N, N]`.
    compute_v: An optional `bool`. Defaults to `True`.
      If `True` then eigenvectors will be computed and returned in `v`.
      Otherwise, only the eigenvalues will be computed.
    name: A name for the operation (optional).

  Returns:
    A tuple of `Tensor` objects (e, v).

    e: A `Tensor`. Has the same type as `input`.
    v: A `Tensor`. Has the same type as `input`.
  """
  _ctx = _context._context or _context.context()
  tld = _ctx._thread_local_data
  if tld.is_eager:
    try:
      _result = pywrap_tfe.TFE_Py_FastPathExecute(
        _ctx._context_handle, tld.device_name, "SelfAdjointEigV2", name,
        tld.op_callbacks, input, "compute_v", compute_v)
      _result = _SelfAdjointEigV2Output._make(_result)
      return _result
    except _core._FallbackException:
      try:
        return self_adjoint_eig_v2_eager_fallback(
            input, compute_v=compute_v, name=name, ctx=_ctx)
      except _core._SymbolicException:
        pass  # Add nodes to the TensorFlow graph.
    except _core._NotOkStatusException as e:
      _ops.raise_from_not_ok_status(e, name)
  # Add nodes to the TensorFlow graph.
  if compute_v is None:
    compute_v = True
  compute_v = _execute.make_bool(compute_v, "compute_v")
  _, _, _op, _outputs = _op_def_library._apply_op_helper(
        "SelfAdjointEigV2", input=input, compute_v=compute_v, name=name)
  _result = _outputs[:]
  if _execute.must_record_gradient():
    _attrs = ("compute_v", _op._get_attr_bool("compute_v"), "T",
              _op._get_attr_type("T"))
    _inputs_flat = _op.inputs
    _execute.record_gradient(
        "SelfAdjointEigV2", _inputs_flat, _attrs, _result)
  _result = _SelfAdjointEigV2Output._make(_result)
  return _result

SelfAdjointEigV2 = tf_export("raw_ops.SelfAdjointEigV2")(_ops.to_raw_op(self_adjoint_eig_v2))


def self_adjoint_eig_v2_eager_fallback(input, compute_v, name, ctx):
  if compute_v is None:
    compute_v = True
  compute_v = _execute.make_bool(compute_v, "compute_v")
  _attr_T, (input,) = _execute.args_to_matching_eager([input], ctx)
  _inputs_flat = [input]
  _attrs = ("compute_v", compute_v, "T", _attr_T)
  _result = _execute.execute(b"SelfAdjointEigV2", 2, inputs=_inputs_flat,
                             attrs=_attrs, ctx=ctx, name=name)
  if _execute.must_record_gradient():
    _execute.record_gradient(
        "SelfAdjointEigV2", _inputs_flat, _attrs, _result)
  _result = _SelfAdjointEigV2Output._make(_result)
  return _result

_SvdOutput = collections.namedtuple(
    "Svd",
    ["s", "u", "v"])


def svd(input, compute_uv=True, full_matrices=False, name=None):
  r"""Computes the singular value decompositions of one or more matrices.

  Computes the SVD of each inner matrix in `input` such that
  `input[..., :, :] = u[..., :, :] * diag(s[..., :, :]) * transpose(v[..., :, :])`

  ```python
  # a is a tensor containing a batch of matrices.
  # s is a tensor of singular values for each matrix.
  # u is the tensor containing the left singular vectors for each matrix.
  # v is the tensor containing the right singular vectors for each matrix.
  s, u, v = svd(a)
  s, _, _ = svd(a, compute_uv=False)
  ```

  Args:
    input: A `Tensor`. Must be one of the following types: `float64`, `float32`, `half`, `complex64`, `complex128`.
      A tensor of shape `[..., M, N]` whose inner-most 2 dimensions
      form matrices of size `[M, N]`. Let `P` be the minimum of `M` and `N`.
    compute_uv: An optional `bool`. Defaults to `True`.
      If true, left and right singular vectors will be
      computed and returned in `u` and `v`, respectively.
      If false, `u` and `v` are not set and should never referenced.
    full_matrices: An optional `bool`. Defaults to `False`.
      If true, compute full-sized `u` and `v`. If false
      (the default), compute only the leading `P` singular vectors.
      Ignored if `compute_uv` is `False`.
    name: A name for the operation (optional).

  Returns:
    A tuple of `Tensor` objects (s, u, v).

    s: A `Tensor`. Has the same type as `input`.
    u: A `Tensor`. Has the same type as `input`.
    v: A `Tensor`. Has the same type as `input`.
  """
  _ctx = _context._context or _context.context()
  tld = _ctx._thread_local_data
  if tld.is_eager:
    try:
      _result = pywrap_tfe.TFE_Py_FastPathExecute(
        _ctx._context_handle, tld.device_name, "Svd", name, tld.op_callbacks,
        input, "compute_uv", compute_uv, "full_matrices", full_matrices)
      _result = _SvdOutput._make(_result)
      return _result
    except _core._FallbackException:
      try:
        return svd_eager_fallback(
            input, compute_uv=compute_uv, full_matrices=full_matrices,
            name=name, ctx=_ctx)
      except _core._SymbolicException:
        pass  # Add nodes to the TensorFlow graph.
    except _core._NotOkStatusException as e:
      _ops.raise_from_not_ok_status(e, name)
  # Add nodes to the TensorFlow graph.
  if compute_uv is None:
    compute_uv = True
  compute_uv = _execute.make_bool(compute_uv, "compute_uv")
  if full_matrices is None:
    full_matrices = False
  full_matrices = _execute.make_bool(full_matrices, "full_matrices")
  _, _, _op, _outputs = _op_def_library._apply_op_helper(
        "Svd", input=input, compute_uv=compute_uv,
               full_matrices=full_matrices, name=name)
  _result = _outputs[:]
  if _execute.must_record_gradient():
    _attrs = ("compute_uv", _op._get_attr_bool("compute_uv"), "full_matrices",
              _op._get_attr_bool("full_matrices"), "T",
              _op._get_attr_type("T"))
    _inputs_flat = _op.inputs
    _execute.record_gradient(
        "Svd", _inputs_flat, _attrs, _result)
  _result = _SvdOutput._make(_result)
  return _result

Svd = tf_export("raw_ops.Svd")(_ops.to_raw_op(svd))


def svd_eager_fallback(input, compute_uv, full_matrices, name, ctx):
  if compute_uv is None:
    compute_uv = True
  compute_uv = _execute.make_bool(compute_uv, "compute_uv")
  if full_matrices is None:
    full_matrices = False
  full_matrices = _execute.make_bool(full_matrices, "full_matrices")
  _attr_T, (input,) = _execute.args_to_matching_eager([input], ctx)
  _inputs_flat = [input]
  _attrs = ("compute_uv", compute_uv, "full_matrices", full_matrices, "T",
  _attr_T)
  _result = _execute.execute(b"Svd", 3, inputs=_inputs_flat, attrs=_attrs,
                             ctx=ctx, name=name)
  if _execute.must_record_gradient():
    _execute.record_gradient(
        "Svd", _inputs_flat, _attrs, _result)
  _result = _SvdOutput._make(_result)
  return _result


def tridiagonal_mat_mul(superdiag, maindiag, subdiag, rhs, name=None):
  r"""Calculate product with tridiagonal matrix.

  Calculates product of two matrices, where left matrix is a tridiagonal matrix.

  Args:
    superdiag: A `Tensor`. Must be one of the following types: `float64`, `float32`, `complex64`, `complex128`.
      Tensor of shape `[..., 1, M]`, representing superdiagonals of
      tri-diagonal matrices to the left of multiplication. Last element is ignored.
    maindiag: A `Tensor`. Must have the same type as `superdiag`.
      Tensor of shape `[..., 1, M]`, representing main diagonals of tri-diagonal
      matrices to the left of multiplication.
    subdiag: A `Tensor`. Must have the same type as `superdiag`.
      Tensor of shape `[..., 1, M]`, representing subdiagonals of tri-diagonal
      matrices to the left of multiplication. First element is ignored.
    rhs: A `Tensor`. Must have the same type as `superdiag`.
      Tensor of shape `[..., M, N]`, representing MxN matrices to the right of
      multiplication.
    name: A name for the operation (optional).

  Returns:
    A `Tensor`. Has the same type as `superdiag`.
  """
  _ctx = _context._context or _context.context()
  tld = _ctx._thread_local_data
  if tld.is_eager:
    try:
      _result = pywrap_tfe.TFE_Py_FastPathExecute(
        _ctx._context_handle, tld.device_name, "TridiagonalMatMul", name,
        tld.op_callbacks, superdiag, maindiag, subdiag, rhs)
      return _result
    except _core._FallbackException:
      try:
        return tridiagonal_mat_mul_eager_fallback(
            superdiag, maindiag, subdiag, rhs, name=name, ctx=_ctx)
      except _core._SymbolicException:
        pass  # Add nodes to the TensorFlow graph.
    except _core._NotOkStatusException as e:
      _ops.raise_from_not_ok_status(e, name)
  # Add nodes to the TensorFlow graph.
  _, _, _op, _outputs = _op_def_library._apply_op_helper(
        "TridiagonalMatMul", superdiag=superdiag, maindiag=maindiag,
                             subdiag=subdiag, rhs=rhs, name=name)
  _result = _outputs[:]
  if _execute.must_record_gradient():
    _attrs = ("T", _op._get_attr_type("T"))
    _inputs_flat = _op.inputs
    _execute.record_gradient(
        "TridiagonalMatMul", _inputs_flat, _attrs, _result)
  _result, = _result
  return _result

TridiagonalMatMul = tf_export("raw_ops.TridiagonalMatMul")(_ops.to_raw_op(tridiagonal_mat_mul))


def tridiagonal_mat_mul_eager_fallback(superdiag, maindiag, subdiag, rhs, name, ctx):
  _attr_T, _inputs_T = _execute.args_to_matching_eager([superdiag, maindiag, subdiag, rhs], ctx)
  (superdiag, maindiag, subdiag, rhs) = _inputs_T
  _inputs_flat = [superdiag, maindiag, subdiag, rhs]
  _attrs = ("T", _attr_T)
  _result = _execute.execute(b"TridiagonalMatMul", 1, inputs=_inputs_flat,
                             attrs=_attrs, ctx=ctx, name=name)
  if _execute.must_record_gradient():
    _execute.record_gradient(
        "TridiagonalMatMul", _inputs_flat, _attrs, _result)
  _result, = _result
  return _result


def tridiagonal_solve(diagonals, rhs, partial_pivoting=True, name=None):
  r"""Solves tridiagonal systems of equations.

    Solves tridiagonal systems of equations.
    Supports batch dimensions and multiple right-hand sides per each left-hand
    side.
    On CPU, solution is computed via Gaussian elimination with or without partial
    pivoting, depending on `partial_pivoting` attribute. On GPU, Nvidia's cuSPARSE
    library is used: https://docs.nvidia.com/cuda/cusparse/index.html#gtsv

  Args:
    diagonals: A `Tensor`. Must be one of the following types: `float64`, `float32`, `complex64`, `complex128`.
      Tensor of shape `[..., 3, M]` whose innermost 2 dimensions represent the
      tridiagonal matrices with three rows being the superdiagonal, diagonals, and
      subdiagonals, in order. The last element of the superdiagonal and the first
      element of the subdiagonal is ignored.
    rhs: A `Tensor`. Must have the same type as `diagonals`.
      Tensor of shape `[..., M, K]`, representing K right-hand sides per each
      left-hand side.
    partial_pivoting: An optional `bool`. Defaults to `True`.
      Whether to apply partial pivoting. Partial pivoting makes the procedure more
      stable, but slower.
    name: A name for the operation (optional).

  Returns:
    A `Tensor`. Has the same type as `diagonals`.
  """
  _ctx = _context._context or _context.context()
  tld = _ctx._thread_local_data
  if tld.is_eager:
    try:
      _result = pywrap_tfe.TFE_Py_FastPathExecute(
        _ctx._context_handle, tld.device_name, "TridiagonalSolve", name,
        tld.op_callbacks, diagonals, rhs, "partial_pivoting",
        partial_pivoting)
      return _result
    except _core._FallbackException:
      try:
        return tridiagonal_solve_eager_fallback(
            diagonals, rhs, partial_pivoting=partial_pivoting, name=name,
            ctx=_ctx)
      except _core._SymbolicException:
        pass  # Add nodes to the TensorFlow graph.
    except _core._NotOkStatusException as e:
      _ops.raise_from_not_ok_status(e, name)
  # Add nodes to the TensorFlow graph.
  if partial_pivoting is None:
    partial_pivoting = True
  partial_pivoting = _execute.make_bool(partial_pivoting, "partial_pivoting")
  _, _, _op, _outputs = _op_def_library._apply_op_helper(
        "TridiagonalSolve", diagonals=diagonals, rhs=rhs,
                            partial_pivoting=partial_pivoting, name=name)
  _result = _outputs[:]
  if _execute.must_record_gradient():
    _attrs = ("partial_pivoting", _op._get_attr_bool("partial_pivoting"), "T",
              _op._get_attr_type("T"))
    _inputs_flat = _op.inputs
    _execute.record_gradient(
        "TridiagonalSolve", _inputs_flat, _attrs, _result)
  _result, = _result
  return _result

TridiagonalSolve = tf_export("raw_ops.TridiagonalSolve")(_ops.to_raw_op(tridiagonal_solve))


def tridiagonal_solve_eager_fallback(diagonals, rhs, partial_pivoting, name, ctx):
  if partial_pivoting is None:
    partial_pivoting = True
  partial_pivoting = _execute.make_bool(partial_pivoting, "partial_pivoting")
  _attr_T, _inputs_T = _execute.args_to_matching_eager([diagonals, rhs], ctx)
  (diagonals, rhs) = _inputs_T
  _inputs_flat = [diagonals, rhs]
  _attrs = ("partial_pivoting", partial_pivoting, "T", _attr_T)
  _result = _execute.execute(b"TridiagonalSolve", 1, inputs=_inputs_flat,
                             attrs=_attrs, ctx=ctx, name=name)
  if _execute.must_record_gradient():
    _execute.record_gradient(
        "TridiagonalSolve", _inputs_flat, _attrs, _result)
  _result, = _result
  return _result

