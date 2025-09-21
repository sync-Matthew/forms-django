from .models import Form, Section, Row, Field
from .schemas import (
    CREATE_FORM_SCHEMA,
    READ_FORM_SCHEMA,
    CREATE_SECTION_SCHEMA,
    READ_SECTION_SCHEMA,
    CREATE_ROW_SCHEMA,
    READ_ROW_SCHEMA,
    CREATE_FIELD_SCHEMA,
    READ_FIELD_SCHEMA,
)
from drf_spectacular.utils import extend_schema_serializer, OpenApiExample
from rest_framework import serializers


@extend_schema_serializer(
    examples=[
        OpenApiExample(
            name="Request Example",
            value=CREATE_FORM_SCHEMA,
            request_only=True,
        ),
    ],
)
class FormCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Form
        fields = [
            "title",
            "description",
        ]

    def create(self, validated_data):
        user = self.context['request'].user
        return Form.objects.create(
            **validated_data,
            user_id=user.id,
        )


@extend_schema_serializer(
    examples=[
        OpenApiExample(
            name="Response Example",
            value=READ_FORM_SCHEMA,
            response_only=True,
        ),
    ],
)
class FormReadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Form
        fields = [
            "id",
            "title",
            "description",
            "created_at",
            "updated_at",
        ]


@extend_schema_serializer(
    examples=[
        OpenApiExample(
            name="Request Example",
            value=CREATE_SECTION_SCHEMA,
            request_only=True,
        ),
    ],
)
class SectionCreateSerializer(serializers.ModelSerializer):
    form_id = serializers.PrimaryKeyRelatedField(
        write_only=True, 
        queryset=Form.objects.all(), 
        source="form",
    )
    class Meta:
        model = Section
        fields = [
            "form_id",
            "title",
            "position",
        ]


@extend_schema_serializer(
    examples=[
        OpenApiExample(
            name="Response Example",
            value=READ_SECTION_SCHEMA,
            response_only=True,
        ),
    ],
)
class SectionReadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Section
        fields = [
            "id",
            "form_id",
            "title",
            "position",
            "created_at",
            "updated_at",
        ]