# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: tensorflow/core/protobuf/device_properties.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='tensorflow/core/protobuf/device_properties.proto',
  package='tensorflow',
  syntax='proto3',
  serialized_options=_b('B\026DevicePropertiesProtosZHgithub.com/tensorflow/tensorflow/tensorflow/go/core/core_protos_go_proto\370\001\001'),
  serialized_pb=_b('\n0tensorflow/core/protobuf/device_properties.proto\x12\ntensorflow\"\x90\x03\n\x10\x44\x65viceProperties\x12\x0c\n\x04type\x18\x01 \x01(\t\x12\x0e\n\x06vendor\x18\x02 \x01(\t\x12\r\n\x05model\x18\x03 \x01(\t\x12\x11\n\tfrequency\x18\x04 \x01(\x03\x12\x11\n\tnum_cores\x18\x05 \x01(\x03\x12\x42\n\x0b\x65nvironment\x18\x06 \x03(\x0b\x32-.tensorflow.DeviceProperties.EnvironmentEntry\x12\x15\n\rnum_registers\x18\x07 \x01(\x03\x12\x15\n\rl1_cache_size\x18\x08 \x01(\x03\x12\x15\n\rl2_cache_size\x18\t \x01(\x03\x12\x15\n\rl3_cache_size\x18\n \x01(\x03\x12-\n%shared_memory_size_per_multiprocessor\x18\x0b \x01(\x03\x12\x13\n\x0bmemory_size\x18\x0c \x01(\x03\x12\x11\n\tbandwidth\x18\r \x01(\x03\x1a\x32\n\x10\x45nvironmentEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"M\n\x0bNamedDevice\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x30\n\nproperties\x18\x02 \x01(\x0b\x32\x1c.tensorflow.DevicePropertiesBeB\x16\x44\x65vicePropertiesProtosZHgithub.com/tensorflow/tensorflow/tensorflow/go/core/core_protos_go_proto\xf8\x01\x01\x62\x06proto3')
)




_DEVICEPROPERTIES_ENVIRONMENTENTRY = _descriptor.Descriptor(
  name='EnvironmentEntry',
  full_name='tensorflow.DeviceProperties.EnvironmentEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='tensorflow.DeviceProperties.EnvironmentEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='tensorflow.DeviceProperties.EnvironmentEntry.value', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=_b('8\001'),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=415,
  serialized_end=465,
)

_DEVICEPROPERTIES = _descriptor.Descriptor(
  name='DeviceProperties',
  full_name='tensorflow.DeviceProperties',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='type', full_name='tensorflow.DeviceProperties.type', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='vendor', full_name='tensorflow.DeviceProperties.vendor', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='model', full_name='tensorflow.DeviceProperties.model', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='frequency', full_name='tensorflow.DeviceProperties.frequency', index=3,
      number=4, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='num_cores', full_name='tensorflow.DeviceProperties.num_cores', index=4,
      number=5, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='environment', full_name='tensorflow.DeviceProperties.environment', index=5,
      number=6, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='num_registers', full_name='tensorflow.DeviceProperties.num_registers', index=6,
      number=7, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='l1_cache_size', full_name='tensorflow.DeviceProperties.l1_cache_size', index=7,
      number=8, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='l2_cache_size', full_name='tensorflow.DeviceProperties.l2_cache_size', index=8,
      number=9, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='l3_cache_size', full_name='tensorflow.DeviceProperties.l3_cache_size', index=9,
      number=10, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='shared_memory_size_per_multiprocessor', full_name='tensorflow.DeviceProperties.shared_memory_size_per_multiprocessor', index=10,
      number=11, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='memory_size', full_name='tensorflow.DeviceProperties.memory_size', index=11,
      number=12, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='bandwidth', full_name='tensorflow.DeviceProperties.bandwidth', index=12,
      number=13, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_DEVICEPROPERTIES_ENVIRONMENTENTRY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=65,
  serialized_end=465,
)


_NAMEDDEVICE = _descriptor.Descriptor(
  name='NamedDevice',
  full_name='tensorflow.NamedDevice',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='tensorflow.NamedDevice.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='properties', full_name='tensorflow.NamedDevice.properties', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=467,
  serialized_end=544,
)

_DEVICEPROPERTIES_ENVIRONMENTENTRY.containing_type = _DEVICEPROPERTIES
_DEVICEPROPERTIES.fields_by_name['environment'].message_type = _DEVICEPROPERTIES_ENVIRONMENTENTRY
_NAMEDDEVICE.fields_by_name['properties'].message_type = _DEVICEPROPERTIES
DESCRIPTOR.message_types_by_name['DeviceProperties'] = _DEVICEPROPERTIES
DESCRIPTOR.message_types_by_name['NamedDevice'] = _NAMEDDEVICE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

DeviceProperties = _reflection.GeneratedProtocolMessageType('DeviceProperties', (_message.Message,), {

  'EnvironmentEntry' : _reflection.GeneratedProtocolMessageType('EnvironmentEntry', (_message.Message,), {
    'DESCRIPTOR' : _DEVICEPROPERTIES_ENVIRONMENTENTRY,
    '__module__' : 'tensorflow.core.protobuf.device_properties_pb2'
    # @@protoc_insertion_point(class_scope:tensorflow.DeviceProperties.EnvironmentEntry)
    })
  ,
  'DESCRIPTOR' : _DEVICEPROPERTIES,
  '__module__' : 'tensorflow.core.protobuf.device_properties_pb2'
  # @@protoc_insertion_point(class_scope:tensorflow.DeviceProperties)
  })
_sym_db.RegisterMessage(DeviceProperties)
_sym_db.RegisterMessage(DeviceProperties.EnvironmentEntry)

NamedDevice = _reflection.GeneratedProtocolMessageType('NamedDevice', (_message.Message,), {
  'DESCRIPTOR' : _NAMEDDEVICE,
  '__module__' : 'tensorflow.core.protobuf.device_properties_pb2'
  # @@protoc_insertion_point(class_scope:tensorflow.NamedDevice)
  })
_sym_db.RegisterMessage(NamedDevice)


DESCRIPTOR._options = None
_DEVICEPROPERTIES_ENVIRONMENTENTRY._options = None
# @@protoc_insertion_point(module_scope)
