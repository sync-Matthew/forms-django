from .models import UserProfile
from .schemas import (
    CREATE_PROFILE_SCHEMA,
    READ_PROFILE_SCHEMA,
    UPDATE_PROFILE_SCHEMA,
)
from drf_spectacular.utils import extend_schema_serializer, OpenApiExample
from rest_framework import serializers


@extend_schema_serializer(
    examples=[
        OpenApiExample(
            name="Request Example",
            value=CREATE_PROFILE_SCHEMA,
            request_only=True,
        ),
    ],
)
class UserProfileCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = [
            "user_token",
        ]

    def create(self, validated_data):
        user = self.context['request'].user
        return UserProfile.objects.create(
            **validated_data,
            user_id=user.id,
            realm_id=user.realm_id,
            realm=user.realm,
        )

@extend_schema_serializer(
    examples=[
        OpenApiExample(
            name="Response Example",
            value=READ_PROFILE_SCHEMA,
            response_only=True,
        ),
    ],
)
class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = "__all__"


@extend_schema_serializer(
    examples=[
        OpenApiExample(
            name="Update Request Example",
            value=UPDATE_PROFILE_SCHEMA,
            request_only=True,
        ),
    ],
)
class UserProfileUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = [
            "user_token",
        ]
