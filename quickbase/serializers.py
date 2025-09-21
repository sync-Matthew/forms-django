from rest_framework import serializers
from drf_spectacular.utils import extend_schema_serializer, OpenApiExample
from .schemas import (
    APP_SCHEMA,
    TABLE_SCHEMA,
    FIELD_SCHEMA,
)

@extend_schema_serializer(
    examples=[
        OpenApiExample(
            name="Response Example",
            value=APP_SCHEMA,
            response_only=True,
        ),
    ],
)
class QuickbaseAppSerializer(serializers.Serializer):
    id = serializers.CharField()
    name = serializers.CharField()


@extend_schema_serializer(
    examples=[
        OpenApiExample(
            name="Response Example",
            value=TABLE_SCHEMA,
            response_only=True,
        ),
    ],
)
class QuickbaseTableSerializer(serializers.Serializer):
    id = serializers.CharField()
    name = serializers.CharField()
    description = serializers.CharField()


@extend_schema_serializer(
    examples=[
        OpenApiExample(
            name="Response Example",
            value=FIELD_SCHEMA,
            response_only=True,
        ),
    ],
)
class QuickbaseFieldSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    label = serializers.CharField()
    fieldType = serializers.CharField()
    required = serializers.BooleanField()
    properties = serializers.DictField()
