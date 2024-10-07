from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class FeatureCollectionPBuffer(_message.Message):
    __slots__ = ("version", "queryResult")
    class GeometryType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        esriGeometryTypePoint: _ClassVar[FeatureCollectionPBuffer.GeometryType]
        esriGeometryTypeMultipoint: _ClassVar[FeatureCollectionPBuffer.GeometryType]
        esriGeometryTypePolyline: _ClassVar[FeatureCollectionPBuffer.GeometryType]
        esriGeometryTypePolygon: _ClassVar[FeatureCollectionPBuffer.GeometryType]
        esriGeometryTypeMultipatch: _ClassVar[FeatureCollectionPBuffer.GeometryType]
        esriGeometryTypeNone: _ClassVar[FeatureCollectionPBuffer.GeometryType]
        esriGeometryTypeEnvelope: _ClassVar[FeatureCollectionPBuffer.GeometryType]
    esriGeometryTypePoint: FeatureCollectionPBuffer.GeometryType
    esriGeometryTypeMultipoint: FeatureCollectionPBuffer.GeometryType
    esriGeometryTypePolyline: FeatureCollectionPBuffer.GeometryType
    esriGeometryTypePolygon: FeatureCollectionPBuffer.GeometryType
    esriGeometryTypeMultipatch: FeatureCollectionPBuffer.GeometryType
    esriGeometryTypeNone: FeatureCollectionPBuffer.GeometryType
    esriGeometryTypeEnvelope: FeatureCollectionPBuffer.GeometryType
    class FieldType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        esriFieldTypeSmallInteger: _ClassVar[FeatureCollectionPBuffer.FieldType]
        esriFieldTypeInteger: _ClassVar[FeatureCollectionPBuffer.FieldType]
        esriFieldTypeSingle: _ClassVar[FeatureCollectionPBuffer.FieldType]
        esriFieldTypeDouble: _ClassVar[FeatureCollectionPBuffer.FieldType]
        esriFieldTypeString: _ClassVar[FeatureCollectionPBuffer.FieldType]
        esriFieldTypeDate: _ClassVar[FeatureCollectionPBuffer.FieldType]
        esriFieldTypeOID: _ClassVar[FeatureCollectionPBuffer.FieldType]
        esriFieldTypeGeometry: _ClassVar[FeatureCollectionPBuffer.FieldType]
        esriFieldTypeBlob: _ClassVar[FeatureCollectionPBuffer.FieldType]
        esriFieldTypeRaster: _ClassVar[FeatureCollectionPBuffer.FieldType]
        esriFieldTypeGUID: _ClassVar[FeatureCollectionPBuffer.FieldType]
        esriFieldTypeGlobalID: _ClassVar[FeatureCollectionPBuffer.FieldType]
        esriFieldTypeXML: _ClassVar[FeatureCollectionPBuffer.FieldType]
        esriFieldTypeBigInteger: _ClassVar[FeatureCollectionPBuffer.FieldType]
        esriFieldTypeDateOnly: _ClassVar[FeatureCollectionPBuffer.FieldType]
        esriFieldTypeTimeOnly: _ClassVar[FeatureCollectionPBuffer.FieldType]
        esriFieldTypeTimestampOffset: _ClassVar[FeatureCollectionPBuffer.FieldType]
    esriFieldTypeSmallInteger: FeatureCollectionPBuffer.FieldType
    esriFieldTypeInteger: FeatureCollectionPBuffer.FieldType
    esriFieldTypeSingle: FeatureCollectionPBuffer.FieldType
    esriFieldTypeDouble: FeatureCollectionPBuffer.FieldType
    esriFieldTypeString: FeatureCollectionPBuffer.FieldType
    esriFieldTypeDate: FeatureCollectionPBuffer.FieldType
    esriFieldTypeOID: FeatureCollectionPBuffer.FieldType
    esriFieldTypeGeometry: FeatureCollectionPBuffer.FieldType
    esriFieldTypeBlob: FeatureCollectionPBuffer.FieldType
    esriFieldTypeRaster: FeatureCollectionPBuffer.FieldType
    esriFieldTypeGUID: FeatureCollectionPBuffer.FieldType
    esriFieldTypeGlobalID: FeatureCollectionPBuffer.FieldType
    esriFieldTypeXML: FeatureCollectionPBuffer.FieldType
    esriFieldTypeBigInteger: FeatureCollectionPBuffer.FieldType
    esriFieldTypeDateOnly: FeatureCollectionPBuffer.FieldType
    esriFieldTypeTimeOnly: FeatureCollectionPBuffer.FieldType
    esriFieldTypeTimestampOffset: FeatureCollectionPBuffer.FieldType
    class SQLType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        sqlTypeBigInt: _ClassVar[FeatureCollectionPBuffer.SQLType]
        sqlTypeBinary: _ClassVar[FeatureCollectionPBuffer.SQLType]
        sqlTypeBit: _ClassVar[FeatureCollectionPBuffer.SQLType]
        sqlTypeChar: _ClassVar[FeatureCollectionPBuffer.SQLType]
        sqlTypeDate: _ClassVar[FeatureCollectionPBuffer.SQLType]
        sqlTypeDecimal: _ClassVar[FeatureCollectionPBuffer.SQLType]
        sqlTypeDouble: _ClassVar[FeatureCollectionPBuffer.SQLType]
        sqlTypeFloat: _ClassVar[FeatureCollectionPBuffer.SQLType]
        sqlTypeGeometry: _ClassVar[FeatureCollectionPBuffer.SQLType]
        sqlTypeGUID: _ClassVar[FeatureCollectionPBuffer.SQLType]
        sqlTypeInteger: _ClassVar[FeatureCollectionPBuffer.SQLType]
        sqlTypeLongNVarchar: _ClassVar[FeatureCollectionPBuffer.SQLType]
        sqlTypeLongVarbinary: _ClassVar[FeatureCollectionPBuffer.SQLType]
        sqlTypeLongVarchar: _ClassVar[FeatureCollectionPBuffer.SQLType]
        sqlTypeNChar: _ClassVar[FeatureCollectionPBuffer.SQLType]
        sqlTypeNVarchar: _ClassVar[FeatureCollectionPBuffer.SQLType]
        sqlTypeOther: _ClassVar[FeatureCollectionPBuffer.SQLType]
        sqlTypeReal: _ClassVar[FeatureCollectionPBuffer.SQLType]
        sqlTypeSmallInt: _ClassVar[FeatureCollectionPBuffer.SQLType]
        sqlTypeSqlXml: _ClassVar[FeatureCollectionPBuffer.SQLType]
        sqlTypeTime: _ClassVar[FeatureCollectionPBuffer.SQLType]
        sqlTypeTimestamp: _ClassVar[FeatureCollectionPBuffer.SQLType]
        sqlTypeTimestamp2: _ClassVar[FeatureCollectionPBuffer.SQLType]
        sqlTypeTinyInt: _ClassVar[FeatureCollectionPBuffer.SQLType]
        sqlTypeVarbinary: _ClassVar[FeatureCollectionPBuffer.SQLType]
        sqlTypeVarchar: _ClassVar[FeatureCollectionPBuffer.SQLType]
        sqlTypeTimestampWithTimezone: _ClassVar[FeatureCollectionPBuffer.SQLType]
    sqlTypeBigInt: FeatureCollectionPBuffer.SQLType
    sqlTypeBinary: FeatureCollectionPBuffer.SQLType
    sqlTypeBit: FeatureCollectionPBuffer.SQLType
    sqlTypeChar: FeatureCollectionPBuffer.SQLType
    sqlTypeDate: FeatureCollectionPBuffer.SQLType
    sqlTypeDecimal: FeatureCollectionPBuffer.SQLType
    sqlTypeDouble: FeatureCollectionPBuffer.SQLType
    sqlTypeFloat: FeatureCollectionPBuffer.SQLType
    sqlTypeGeometry: FeatureCollectionPBuffer.SQLType
    sqlTypeGUID: FeatureCollectionPBuffer.SQLType
    sqlTypeInteger: FeatureCollectionPBuffer.SQLType
    sqlTypeLongNVarchar: FeatureCollectionPBuffer.SQLType
    sqlTypeLongVarbinary: FeatureCollectionPBuffer.SQLType
    sqlTypeLongVarchar: FeatureCollectionPBuffer.SQLType
    sqlTypeNChar: FeatureCollectionPBuffer.SQLType
    sqlTypeNVarchar: FeatureCollectionPBuffer.SQLType
    sqlTypeOther: FeatureCollectionPBuffer.SQLType
    sqlTypeReal: FeatureCollectionPBuffer.SQLType
    sqlTypeSmallInt: FeatureCollectionPBuffer.SQLType
    sqlTypeSqlXml: FeatureCollectionPBuffer.SQLType
    sqlTypeTime: FeatureCollectionPBuffer.SQLType
    sqlTypeTimestamp: FeatureCollectionPBuffer.SQLType
    sqlTypeTimestamp2: FeatureCollectionPBuffer.SQLType
    sqlTypeTinyInt: FeatureCollectionPBuffer.SQLType
    sqlTypeVarbinary: FeatureCollectionPBuffer.SQLType
    sqlTypeVarchar: FeatureCollectionPBuffer.SQLType
    sqlTypeTimestampWithTimezone: FeatureCollectionPBuffer.SQLType
    class QuantizeOriginPostion(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        upperLeft: _ClassVar[FeatureCollectionPBuffer.QuantizeOriginPostion]
        lowerLeft: _ClassVar[FeatureCollectionPBuffer.QuantizeOriginPostion]
    upperLeft: FeatureCollectionPBuffer.QuantizeOriginPostion
    lowerLeft: FeatureCollectionPBuffer.QuantizeOriginPostion
    class SegmentType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        line: _ClassVar[FeatureCollectionPBuffer.SegmentType]
        arc: _ClassVar[FeatureCollectionPBuffer.SegmentType]
        bezier: _ClassVar[FeatureCollectionPBuffer.SegmentType]
        ellipticArc: _ClassVar[FeatureCollectionPBuffer.SegmentType]
    line: FeatureCollectionPBuffer.SegmentType
    arc: FeatureCollectionPBuffer.SegmentType
    bezier: FeatureCollectionPBuffer.SegmentType
    ellipticArc: FeatureCollectionPBuffer.SegmentType
    class SpatialReference(_message.Message):
        __slots__ = ("wkid", "lastestWkid", "vcsWkid", "latestVcsWkid", "wkt", "wkt2")
        WKID_FIELD_NUMBER: _ClassVar[int]
        LASTESTWKID_FIELD_NUMBER: _ClassVar[int]
        VCSWKID_FIELD_NUMBER: _ClassVar[int]
        LATESTVCSWKID_FIELD_NUMBER: _ClassVar[int]
        WKT_FIELD_NUMBER: _ClassVar[int]
        WKT2_FIELD_NUMBER: _ClassVar[int]
        wkid: int
        lastestWkid: int
        vcsWkid: int
        latestVcsWkid: int
        wkt: str
        wkt2: str
        def __init__(self, wkid: _Optional[int] = ..., lastestWkid: _Optional[int] = ..., vcsWkid: _Optional[int] = ..., latestVcsWkid: _Optional[int] = ..., wkt: _Optional[str] = ..., wkt2: _Optional[str] = ...) -> None: ...
    class Field(_message.Message):
        __slots__ = ("name", "fieldType", "alias", "sqlType", "domain", "defaultValue")
        NAME_FIELD_NUMBER: _ClassVar[int]
        FIELDTYPE_FIELD_NUMBER: _ClassVar[int]
        ALIAS_FIELD_NUMBER: _ClassVar[int]
        SQLTYPE_FIELD_NUMBER: _ClassVar[int]
        DOMAIN_FIELD_NUMBER: _ClassVar[int]
        DEFAULTVALUE_FIELD_NUMBER: _ClassVar[int]
        name: str
        fieldType: FeatureCollectionPBuffer.FieldType
        alias: str
        sqlType: FeatureCollectionPBuffer.SQLType
        domain: str
        defaultValue: str
        def __init__(self, name: _Optional[str] = ..., fieldType: _Optional[_Union[FeatureCollectionPBuffer.FieldType, str]] = ..., alias: _Optional[str] = ..., sqlType: _Optional[_Union[FeatureCollectionPBuffer.SQLType, str]] = ..., domain: _Optional[str] = ..., defaultValue: _Optional[str] = ...) -> None: ...
    class GeometryField(_message.Message):
        __slots__ = ("field", "geometryType")
        FIELD_FIELD_NUMBER: _ClassVar[int]
        GEOMETRYTYPE_FIELD_NUMBER: _ClassVar[int]
        field: FeatureCollectionPBuffer.Field
        geometryType: FeatureCollectionPBuffer.GeometryType
        def __init__(self, field: _Optional[_Union[FeatureCollectionPBuffer.Field, _Mapping]] = ..., geometryType: _Optional[_Union[FeatureCollectionPBuffer.GeometryType, str]] = ...) -> None: ...
    class Envelope(_message.Message):
        __slots__ = ("XMin", "YMin", "XMax", "YMax", "SpatialReference")
        XMIN_FIELD_NUMBER: _ClassVar[int]
        YMIN_FIELD_NUMBER: _ClassVar[int]
        XMAX_FIELD_NUMBER: _ClassVar[int]
        YMAX_FIELD_NUMBER: _ClassVar[int]
        SPATIALREFERENCE_FIELD_NUMBER: _ClassVar[int]
        XMin: float
        YMin: float
        XMax: float
        YMax: float
        SpatialReference: FeatureCollectionPBuffer.SpatialReference
        def __init__(self, XMin: _Optional[float] = ..., YMin: _Optional[float] = ..., XMax: _Optional[float] = ..., YMax: _Optional[float] = ..., SpatialReference: _Optional[_Union[FeatureCollectionPBuffer.SpatialReference, _Mapping]] = ...) -> None: ...
    class Value(_message.Message):
        __slots__ = ("string_value", "float_value", "double_value", "sint_value", "uint_value", "int64_value", "uint64_value", "sint64_value", "bool_value", "null_value", "index")
        STRING_VALUE_FIELD_NUMBER: _ClassVar[int]
        FLOAT_VALUE_FIELD_NUMBER: _ClassVar[int]
        DOUBLE_VALUE_FIELD_NUMBER: _ClassVar[int]
        SINT_VALUE_FIELD_NUMBER: _ClassVar[int]
        UINT_VALUE_FIELD_NUMBER: _ClassVar[int]
        INT64_VALUE_FIELD_NUMBER: _ClassVar[int]
        UINT64_VALUE_FIELD_NUMBER: _ClassVar[int]
        SINT64_VALUE_FIELD_NUMBER: _ClassVar[int]
        BOOL_VALUE_FIELD_NUMBER: _ClassVar[int]
        NULL_VALUE_FIELD_NUMBER: _ClassVar[int]
        INDEX_FIELD_NUMBER: _ClassVar[int]
        string_value: str
        float_value: float
        double_value: float
        sint_value: int
        uint_value: int
        int64_value: int
        uint64_value: int
        sint64_value: int
        bool_value: bool
        null_value: bool
        index: int
        def __init__(self, string_value: _Optional[str] = ..., float_value: _Optional[float] = ..., double_value: _Optional[float] = ..., sint_value: _Optional[int] = ..., uint_value: _Optional[int] = ..., int64_value: _Optional[int] = ..., uint64_value: _Optional[int] = ..., sint64_value: _Optional[int] = ..., bool_value: bool = ..., null_value: bool = ..., index: _Optional[int] = ...) -> None: ...
    class Geometry(_message.Message):
        __slots__ = ("geometryType", "lengths", "coords", "ids")
        GEOMETRYTYPE_FIELD_NUMBER: _ClassVar[int]
        LENGTHS_FIELD_NUMBER: _ClassVar[int]
        COORDS_FIELD_NUMBER: _ClassVar[int]
        IDS_FIELD_NUMBER: _ClassVar[int]
        geometryType: FeatureCollectionPBuffer.GeometryType
        lengths: _containers.RepeatedScalarFieldContainer[int]
        coords: _containers.RepeatedScalarFieldContainer[int]
        ids: _containers.RepeatedScalarFieldContainer[int]
        def __init__(self, geometryType: _Optional[_Union[FeatureCollectionPBuffer.GeometryType, str]] = ..., lengths: _Optional[_Iterable[int]] = ..., coords: _Optional[_Iterable[int]] = ..., ids: _Optional[_Iterable[int]] = ...) -> None: ...
    class CurveGeometry(_message.Message):
        __slots__ = ("geometryType", "parts", "segmentSets", "coords")
        GEOMETRYTYPE_FIELD_NUMBER: _ClassVar[int]
        PARTS_FIELD_NUMBER: _ClassVar[int]
        SEGMENTSETS_FIELD_NUMBER: _ClassVar[int]
        COORDS_FIELD_NUMBER: _ClassVar[int]
        geometryType: FeatureCollectionPBuffer.GeometryType
        parts: _containers.RepeatedScalarFieldContainer[int]
        segmentSets: _containers.RepeatedCompositeFieldContainer[FeatureCollectionPBuffer.SegmentSet]
        coords: _containers.RepeatedScalarFieldContainer[int]
        def __init__(self, geometryType: _Optional[_Union[FeatureCollectionPBuffer.GeometryType, str]] = ..., parts: _Optional[_Iterable[int]] = ..., segmentSets: _Optional[_Iterable[_Union[FeatureCollectionPBuffer.SegmentSet, _Mapping]]] = ..., coords: _Optional[_Iterable[int]] = ...) -> None: ...
    class SegmentSet(_message.Message):
        __slots__ = ("type", "count", "parameters")
        TYPE_FIELD_NUMBER: _ClassVar[int]
        COUNT_FIELD_NUMBER: _ClassVar[int]
        PARAMETERS_FIELD_NUMBER: _ClassVar[int]
        type: FeatureCollectionPBuffer.SegmentType
        count: int
        parameters: _containers.RepeatedScalarFieldContainer[float]
        def __init__(self, type: _Optional[_Union[FeatureCollectionPBuffer.SegmentType, str]] = ..., count: _Optional[int] = ..., parameters: _Optional[_Iterable[float]] = ...) -> None: ...
    class esriShapeBuffer(_message.Message):
        __slots__ = ("bytes",)
        BYTES_FIELD_NUMBER: _ClassVar[int]
        bytes: bytes
        def __init__(self, bytes: _Optional[bytes] = ...) -> None: ...
    class Feature(_message.Message):
        __slots__ = ("attributes", "geometry", "shapeBuffer", "curveGeometry", "centroid", "aggregateGeometries", "envelope")
        ATTRIBUTES_FIELD_NUMBER: _ClassVar[int]
        GEOMETRY_FIELD_NUMBER: _ClassVar[int]
        SHAPEBUFFER_FIELD_NUMBER: _ClassVar[int]
        CURVEGEOMETRY_FIELD_NUMBER: _ClassVar[int]
        CENTROID_FIELD_NUMBER: _ClassVar[int]
        AGGREGATEGEOMETRIES_FIELD_NUMBER: _ClassVar[int]
        ENVELOPE_FIELD_NUMBER: _ClassVar[int]
        attributes: _containers.RepeatedCompositeFieldContainer[FeatureCollectionPBuffer.Value]
        geometry: FeatureCollectionPBuffer.Geometry
        shapeBuffer: FeatureCollectionPBuffer.esriShapeBuffer
        curveGeometry: FeatureCollectionPBuffer.CurveGeometry
        centroid: FeatureCollectionPBuffer.Geometry
        aggregateGeometries: _containers.RepeatedCompositeFieldContainer[FeatureCollectionPBuffer.Geometry]
        envelope: FeatureCollectionPBuffer.Envelope
        def __init__(self, attributes: _Optional[_Iterable[_Union[FeatureCollectionPBuffer.Value, _Mapping]]] = ..., geometry: _Optional[_Union[FeatureCollectionPBuffer.Geometry, _Mapping]] = ..., shapeBuffer: _Optional[_Union[FeatureCollectionPBuffer.esriShapeBuffer, _Mapping]] = ..., curveGeometry: _Optional[_Union[FeatureCollectionPBuffer.CurveGeometry, _Mapping]] = ..., centroid: _Optional[_Union[FeatureCollectionPBuffer.Geometry, _Mapping]] = ..., aggregateGeometries: _Optional[_Iterable[_Union[FeatureCollectionPBuffer.Geometry, _Mapping]]] = ..., envelope: _Optional[_Union[FeatureCollectionPBuffer.Envelope, _Mapping]] = ...) -> None: ...
    class UniqueIdField(_message.Message):
        __slots__ = ("name", "isSystemMaintained")
        NAME_FIELD_NUMBER: _ClassVar[int]
        ISSYSTEMMAINTAINED_FIELD_NUMBER: _ClassVar[int]
        name: str
        isSystemMaintained: bool
        def __init__(self, name: _Optional[str] = ..., isSystemMaintained: bool = ...) -> None: ...
    class GeometryProperties(_message.Message):
        __slots__ = ("shapeAreaFieldName", "shapeLengthFieldName", "units")
        SHAPEAREAFIELDNAME_FIELD_NUMBER: _ClassVar[int]
        SHAPELENGTHFIELDNAME_FIELD_NUMBER: _ClassVar[int]
        UNITS_FIELD_NUMBER: _ClassVar[int]
        shapeAreaFieldName: str
        shapeLengthFieldName: str
        units: str
        def __init__(self, shapeAreaFieldName: _Optional[str] = ..., shapeLengthFieldName: _Optional[str] = ..., units: _Optional[str] = ...) -> None: ...
    class ServerGens(_message.Message):
        __slots__ = ("minServerGen", "serverGen")
        MINSERVERGEN_FIELD_NUMBER: _ClassVar[int]
        SERVERGEN_FIELD_NUMBER: _ClassVar[int]
        minServerGen: int
        serverGen: int
        def __init__(self, minServerGen: _Optional[int] = ..., serverGen: _Optional[int] = ...) -> None: ...
    class Scale(_message.Message):
        __slots__ = ("xScale", "yScale", "mScale", "zScale")
        XSCALE_FIELD_NUMBER: _ClassVar[int]
        YSCALE_FIELD_NUMBER: _ClassVar[int]
        MSCALE_FIELD_NUMBER: _ClassVar[int]
        ZSCALE_FIELD_NUMBER: _ClassVar[int]
        xScale: float
        yScale: float
        mScale: float
        zScale: float
        def __init__(self, xScale: _Optional[float] = ..., yScale: _Optional[float] = ..., mScale: _Optional[float] = ..., zScale: _Optional[float] = ...) -> None: ...
    class Translate(_message.Message):
        __slots__ = ("xTranslate", "yTranslate", "mTranslate", "zTranslate")
        XTRANSLATE_FIELD_NUMBER: _ClassVar[int]
        YTRANSLATE_FIELD_NUMBER: _ClassVar[int]
        MTRANSLATE_FIELD_NUMBER: _ClassVar[int]
        ZTRANSLATE_FIELD_NUMBER: _ClassVar[int]
        xTranslate: float
        yTranslate: float
        mTranslate: float
        zTranslate: float
        def __init__(self, xTranslate: _Optional[float] = ..., yTranslate: _Optional[float] = ..., mTranslate: _Optional[float] = ..., zTranslate: _Optional[float] = ...) -> None: ...
    class Transform(_message.Message):
        __slots__ = ("quantizeOriginPostion", "scale", "translate")
        QUANTIZEORIGINPOSTION_FIELD_NUMBER: _ClassVar[int]
        SCALE_FIELD_NUMBER: _ClassVar[int]
        TRANSLATE_FIELD_NUMBER: _ClassVar[int]
        quantizeOriginPostion: FeatureCollectionPBuffer.QuantizeOriginPostion
        scale: FeatureCollectionPBuffer.Scale
        translate: FeatureCollectionPBuffer.Translate
        def __init__(self, quantizeOriginPostion: _Optional[_Union[FeatureCollectionPBuffer.QuantizeOriginPostion, str]] = ..., scale: _Optional[_Union[FeatureCollectionPBuffer.Scale, _Mapping]] = ..., translate: _Optional[_Union[FeatureCollectionPBuffer.Translate, _Mapping]] = ...) -> None: ...
    class FeatureResult(_message.Message):
        __slots__ = ("objectIdFieldName", "uniqueIdField", "globalIdFieldName", "geohashFieldName", "geometryProperties", "serverGens", "geometryType", "spatialReference", "exceededTransferLimit", "hasZ", "hasM", "transform", "fields", "values", "features", "geometryFields")
        OBJECTIDFIELDNAME_FIELD_NUMBER: _ClassVar[int]
        UNIQUEIDFIELD_FIELD_NUMBER: _ClassVar[int]
        GLOBALIDFIELDNAME_FIELD_NUMBER: _ClassVar[int]
        GEOHASHFIELDNAME_FIELD_NUMBER: _ClassVar[int]
        GEOMETRYPROPERTIES_FIELD_NUMBER: _ClassVar[int]
        SERVERGENS_FIELD_NUMBER: _ClassVar[int]
        GEOMETRYTYPE_FIELD_NUMBER: _ClassVar[int]
        SPATIALREFERENCE_FIELD_NUMBER: _ClassVar[int]
        EXCEEDEDTRANSFERLIMIT_FIELD_NUMBER: _ClassVar[int]
        HASZ_FIELD_NUMBER: _ClassVar[int]
        HASM_FIELD_NUMBER: _ClassVar[int]
        TRANSFORM_FIELD_NUMBER: _ClassVar[int]
        FIELDS_FIELD_NUMBER: _ClassVar[int]
        VALUES_FIELD_NUMBER: _ClassVar[int]
        FEATURES_FIELD_NUMBER: _ClassVar[int]
        GEOMETRYFIELDS_FIELD_NUMBER: _ClassVar[int]
        objectIdFieldName: str
        uniqueIdField: FeatureCollectionPBuffer.UniqueIdField
        globalIdFieldName: str
        geohashFieldName: str
        geometryProperties: FeatureCollectionPBuffer.GeometryProperties
        serverGens: FeatureCollectionPBuffer.ServerGens
        geometryType: FeatureCollectionPBuffer.GeometryType
        spatialReference: FeatureCollectionPBuffer.SpatialReference
        exceededTransferLimit: bool
        hasZ: bool
        hasM: bool
        transform: FeatureCollectionPBuffer.Transform
        fields: _containers.RepeatedCompositeFieldContainer[FeatureCollectionPBuffer.Field]
        values: _containers.RepeatedCompositeFieldContainer[FeatureCollectionPBuffer.Value]
        features: _containers.RepeatedCompositeFieldContainer[FeatureCollectionPBuffer.Feature]
        geometryFields: _containers.RepeatedCompositeFieldContainer[FeatureCollectionPBuffer.GeometryField]
        def __init__(self, objectIdFieldName: _Optional[str] = ..., uniqueIdField: _Optional[_Union[FeatureCollectionPBuffer.UniqueIdField, _Mapping]] = ..., globalIdFieldName: _Optional[str] = ..., geohashFieldName: _Optional[str] = ..., geometryProperties: _Optional[_Union[FeatureCollectionPBuffer.GeometryProperties, _Mapping]] = ..., serverGens: _Optional[_Union[FeatureCollectionPBuffer.ServerGens, _Mapping]] = ..., geometryType: _Optional[_Union[FeatureCollectionPBuffer.GeometryType, str]] = ..., spatialReference: _Optional[_Union[FeatureCollectionPBuffer.SpatialReference, _Mapping]] = ..., exceededTransferLimit: bool = ..., hasZ: bool = ..., hasM: bool = ..., transform: _Optional[_Union[FeatureCollectionPBuffer.Transform, _Mapping]] = ..., fields: _Optional[_Iterable[_Union[FeatureCollectionPBuffer.Field, _Mapping]]] = ..., values: _Optional[_Iterable[_Union[FeatureCollectionPBuffer.Value, _Mapping]]] = ..., features: _Optional[_Iterable[_Union[FeatureCollectionPBuffer.Feature, _Mapping]]] = ..., geometryFields: _Optional[_Iterable[_Union[FeatureCollectionPBuffer.GeometryField, _Mapping]]] = ...) -> None: ...
    class CountResult(_message.Message):
        __slots__ = ("count",)
        COUNT_FIELD_NUMBER: _ClassVar[int]
        count: int
        def __init__(self, count: _Optional[int] = ...) -> None: ...
    class ObjectIdsResult(_message.Message):
        __slots__ = ("objectIdFieldName", "serverGens", "objectIds")
        OBJECTIDFIELDNAME_FIELD_NUMBER: _ClassVar[int]
        SERVERGENS_FIELD_NUMBER: _ClassVar[int]
        OBJECTIDS_FIELD_NUMBER: _ClassVar[int]
        objectIdFieldName: str
        serverGens: FeatureCollectionPBuffer.ServerGens
        objectIds: _containers.RepeatedScalarFieldContainer[int]
        def __init__(self, objectIdFieldName: _Optional[str] = ..., serverGens: _Optional[_Union[FeatureCollectionPBuffer.ServerGens, _Mapping]] = ..., objectIds: _Optional[_Iterable[int]] = ...) -> None: ...
    class ExtentCountResult(_message.Message):
        __slots__ = ("extent", "count")
        EXTENT_FIELD_NUMBER: _ClassVar[int]
        COUNT_FIELD_NUMBER: _ClassVar[int]
        extent: FeatureCollectionPBuffer.Envelope
        count: int
        def __init__(self, extent: _Optional[_Union[FeatureCollectionPBuffer.Envelope, _Mapping]] = ..., count: _Optional[int] = ...) -> None: ...
    class QueryResult(_message.Message):
        __slots__ = ("featureResult", "countResult", "idsResult", "extentCountResult")
        FEATURERESULT_FIELD_NUMBER: _ClassVar[int]
        COUNTRESULT_FIELD_NUMBER: _ClassVar[int]
        IDSRESULT_FIELD_NUMBER: _ClassVar[int]
        EXTENTCOUNTRESULT_FIELD_NUMBER: _ClassVar[int]
        featureResult: FeatureCollectionPBuffer.FeatureResult
        countResult: FeatureCollectionPBuffer.CountResult
        idsResult: FeatureCollectionPBuffer.ObjectIdsResult
        extentCountResult: FeatureCollectionPBuffer.ExtentCountResult
        def __init__(self, featureResult: _Optional[_Union[FeatureCollectionPBuffer.FeatureResult, _Mapping]] = ..., countResult: _Optional[_Union[FeatureCollectionPBuffer.CountResult, _Mapping]] = ..., idsResult: _Optional[_Union[FeatureCollectionPBuffer.ObjectIdsResult, _Mapping]] = ..., extentCountResult: _Optional[_Union[FeatureCollectionPBuffer.ExtentCountResult, _Mapping]] = ...) -> None: ...
    VERSION_FIELD_NUMBER: _ClassVar[int]
    QUERYRESULT_FIELD_NUMBER: _ClassVar[int]
    version: str
    queryResult: FeatureCollectionPBuffer.QueryResult
    def __init__(self, version: _Optional[str] = ..., queryResult: _Optional[_Union[FeatureCollectionPBuffer.QueryResult, _Mapping]] = ...) -> None: ...
