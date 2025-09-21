from rest_framework import serializers
from drf_spectacular.utils import extend_schema_serializer, OpenApiExample
from .schemas import READ_APPS_SCHEMA, READ_TABLES_SCHEMA, READ_FIELDS_SCHEMA

@extend_schema_serializer(
    examples=[
        OpenApiExample(
            name="Response Example",
            value=READ_APPS_SCHEMA,
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
            value=READ_TABLES_SCHEMA,
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
            value=READ_FIELDS_SCHEMA,
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
