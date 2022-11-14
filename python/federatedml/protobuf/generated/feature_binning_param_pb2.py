# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: feature-binning-param.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1b\x66\x65\x61ture-binning-param.proto\x12&com.webank.ai.fate.core.mlmodel.buffer\"\xa3\x02\n\x07IVParam\x12\x11\n\twoe_array\x18\x01 \x03(\x01\x12\x10\n\x08iv_array\x18\x02 \x03(\x01\x12\x19\n\x11\x65vent_count_array\x18\x03 \x03(\x03\x12\x1d\n\x15non_event_count_array\x18\x04 \x03(\x03\x12\x18\n\x10\x65vent_rate_array\x18\x05 \x03(\x01\x12\x1c\n\x14non_event_rate_array\x18\x06 \x03(\x01\x12\x14\n\x0csplit_points\x18\x07 \x03(\x01\x12\n\n\x02iv\x18\x08 \x01(\x01\x12\x18\n\x10is_woe_monotonic\x18\t \x01(\x08\x12\x10\n\x08\x62in_nums\x18\n \x01(\x03\x12\x15\n\rbin_anonymous\x18\x0b \x03(\t\x12\x1c\n\x14optimal_metric_array\x18\x0c \x03(\x01\"\x86\x02\n\x14\x46\x65\x61tureBinningResult\x12g\n\x0e\x62inning_result\x18\x01 \x03(\x0b\x32O.com.webank.ai.fate.core.mlmodel.buffer.FeatureBinningResult.BinningResultEntry\x12\x0c\n\x04role\x18\x02 \x01(\t\x12\x10\n\x08party_id\x18\x03 \x01(\t\x1a\x65\n\x12\x42inningResultEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12>\n\x05value\x18\x02 \x01(\x0b\x32/.com.webank.ai.fate.core.mlmodel.buffer.IVParam:\x02\x38\x01\"\xf6\x01\n\x10MultiClassResult\x12M\n\x07results\x18\x01 \x03(\x0b\x32<.com.webank.ai.fate.core.mlmodel.buffer.FeatureBinningResult\x12\x0e\n\x06labels\x18\x02 \x03(\t\x12R\n\x0chost_results\x18\x03 \x03(\x0b\x32<.com.webank.ai.fate.core.mlmodel.buffer.FeatureBinningResult\x12\x16\n\x0ehost_party_ids\x18\x04 \x03(\t\x12\x17\n\x0fhas_host_result\x18\x05 \x01(\x08\"R\n\x19\x42inningSingleFeatureValue\x12\x0e\n\x06values\x18\x01 \x03(\x01\x12\x11\n\tcol_names\x18\x02 \x03(\t\x12\x12\n\nvalue_name\x18\x03 \x01(\t\"\xf1\x04\n\x13\x46\x65\x61tureBinningParam\x12T\n\x0e\x62inning_result\x18\x01 \x01(\x0b\x32<.com.webank.ai.fate.core.mlmodel.buffer.FeatureBinningResult\x12R\n\x0chost_results\x18\x02 \x03(\x0b\x32<.com.webank.ai.fate.core.mlmodel.buffer.FeatureBinningResult\x12\x0e\n\x06header\x18\x03 \x03(\t\x12\x18\n\x10header_anonymous\x18\x04 \x03(\t\x12\x12\n\nmodel_name\x18\x05 \x01(\t\x12T\n\x12multi_class_result\x18\x06 \x01(\x0b\x32\x38.com.webank.ai.fate.core.mlmodel.buffer.MultiClassResult\x12^\n\x18transform_binning_result\x18\x07 \x01(\x0b\x32<.com.webank.ai.fate.core.mlmodel.buffer.FeatureBinningResult\x12\\\n\x16transform_host_results\x18\x08 \x03(\x0b\x32<.com.webank.ai.fate.core.mlmodel.buffer.FeatureBinningResult\x12^\n\x1ctransform_multi_class_result\x18\t \x01(\x0b\x32\x38.com.webank.ai.fate.core.mlmodel.buffer.MultiClassResultB\x1a\x42\x18\x46\x65\x61tureBinningParamProtob\x06proto3')



_IVPARAM = DESCRIPTOR.message_types_by_name['IVParam']
_FEATUREBINNINGRESULT = DESCRIPTOR.message_types_by_name['FeatureBinningResult']
_FEATUREBINNINGRESULT_BINNINGRESULTENTRY = _FEATUREBINNINGRESULT.nested_types_by_name['BinningResultEntry']
_MULTICLASSRESULT = DESCRIPTOR.message_types_by_name['MultiClassResult']
_BINNINGSINGLEFEATUREVALUE = DESCRIPTOR.message_types_by_name['BinningSingleFeatureValue']
_FEATUREBINNINGPARAM = DESCRIPTOR.message_types_by_name['FeatureBinningParam']
IVParam = _reflection.GeneratedProtocolMessageType('IVParam', (_message.Message,), {
  'DESCRIPTOR' : _IVPARAM,
  '__module__' : 'feature_binning_param_pb2'
  # @@protoc_insertion_point(class_scope:com.webank.ai.fate.core.mlmodel.buffer.IVParam)
  })
_sym_db.RegisterMessage(IVParam)

FeatureBinningResult = _reflection.GeneratedProtocolMessageType('FeatureBinningResult', (_message.Message,), {

  'BinningResultEntry' : _reflection.GeneratedProtocolMessageType('BinningResultEntry', (_message.Message,), {
    'DESCRIPTOR' : _FEATUREBINNINGRESULT_BINNINGRESULTENTRY,
    '__module__' : 'feature_binning_param_pb2'
    # @@protoc_insertion_point(class_scope:com.webank.ai.fate.core.mlmodel.buffer.FeatureBinningResult.BinningResultEntry)
    })
  ,
  'DESCRIPTOR' : _FEATUREBINNINGRESULT,
  '__module__' : 'feature_binning_param_pb2'
  # @@protoc_insertion_point(class_scope:com.webank.ai.fate.core.mlmodel.buffer.FeatureBinningResult)
  })
_sym_db.RegisterMessage(FeatureBinningResult)
_sym_db.RegisterMessage(FeatureBinningResult.BinningResultEntry)

MultiClassResult = _reflection.GeneratedProtocolMessageType('MultiClassResult', (_message.Message,), {
  'DESCRIPTOR' : _MULTICLASSRESULT,
  '__module__' : 'feature_binning_param_pb2'
  # @@protoc_insertion_point(class_scope:com.webank.ai.fate.core.mlmodel.buffer.MultiClassResult)
  })
_sym_db.RegisterMessage(MultiClassResult)

BinningSingleFeatureValue = _reflection.GeneratedProtocolMessageType('BinningSingleFeatureValue', (_message.Message,), {
  'DESCRIPTOR' : _BINNINGSINGLEFEATUREVALUE,
  '__module__' : 'feature_binning_param_pb2'
  # @@protoc_insertion_point(class_scope:com.webank.ai.fate.core.mlmodel.buffer.BinningSingleFeatureValue)
  })
_sym_db.RegisterMessage(BinningSingleFeatureValue)

FeatureBinningParam = _reflection.GeneratedProtocolMessageType('FeatureBinningParam', (_message.Message,), {
  'DESCRIPTOR' : _FEATUREBINNINGPARAM,
  '__module__' : 'feature_binning_param_pb2'
  # @@protoc_insertion_point(class_scope:com.webank.ai.fate.core.mlmodel.buffer.FeatureBinningParam)
  })
_sym_db.RegisterMessage(FeatureBinningParam)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'B\030FeatureBinningParamProto'
  _FEATUREBINNINGRESULT_BINNINGRESULTENTRY._options = None
  _FEATUREBINNINGRESULT_BINNINGRESULTENTRY._serialized_options = b'8\001'
  _IVPARAM._serialized_start=72
  _IVPARAM._serialized_end=363
  _FEATUREBINNINGRESULT._serialized_start=366
  _FEATUREBINNINGRESULT._serialized_end=628
  _FEATUREBINNINGRESULT_BINNINGRESULTENTRY._serialized_start=527
  _FEATUREBINNINGRESULT_BINNINGRESULTENTRY._serialized_end=628
  _MULTICLASSRESULT._serialized_start=631
  _MULTICLASSRESULT._serialized_end=877
  _BINNINGSINGLEFEATUREVALUE._serialized_start=879
  _BINNINGSINGLEFEATUREVALUE._serialized_end=961
  _FEATUREBINNINGPARAM._serialized_start=964
  _FEATUREBINNINGPARAM._serialized_end=1589
# @@protoc_insertion_point(module_scope)
