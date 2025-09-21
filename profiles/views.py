from .models import UserProfile
from .parameters import UserProfileParameter
from .serializers import (
    UserProfileSerializer,
    UserProfileCreateSerializer,
    UserProfileUpdateSerializer,
)
from api.decorators import suppress_django_filter_warning
from api.schema import CustomStatelessJWTAuthenticationScheme
from django.shortcuts import get_object_or_404
from drf_spectacular.utils import extend_schema_view, extend_schema
from rest_framework import mixins, viewsets, status
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.request import Request


@extend_schema_view(
    create=extend_schema(
        summary="Create a user profile",
    ),
    update=extend_schema(
        summary="Update a user profile",
        parameters=[UserProfileParameter()],
    ),
    partial_update=extend_schema(
        summary="Partial update a user profile",
        parameters=[UserProfileParameter()],
    ),
)
class UserProfileViewSet(
    mixins.CreateModelMixin, 
    mixins.UpdateModelMixin, 
    viewsets.GenericViewSet
):
    """
    A ViewSet for viewing and editing user profiles.
    """

    permission_classes = [IsAuthenticated]

    def get_serializer_class(self):
        if self.action in ["update", "partial_update"]:
            return UserProfileUpdateSerializer
        elif self.action == "create":
            return UserProfileCreateSerializer
        else:
            return UserProfileSerializer

    @suppress_django_filter_warning
    def get_queryset(self):
        user = self.request.user
        if user.is_superuser:
            return UserProfile.objects.all()
        return UserProfile.objects.filter(user_id=user.id)
    
    @extend_schema(summary="Retrieve current authenticated user's profile")
    @action(detail=False, methods=["get"], permission_classes=[IsAuthenticated], url_path="me")
    def me_retrieve(self, request: Request):
        """
        Retrieve the current authenticated user's profile.
        """
        user = request.user
        profile = get_object_or_404(UserProfile, user_id=user.id, realm_id=user.realm_id)
        serializer = UserProfileSerializer(profile)
        data = serializer.data
        return Response(serializer.data, status=status.HTTP_200_OK)

    @extend_schema(
        summary="Partially update the current authenticated user's profile",
        request=UserProfileUpdateSerializer,
        responses={200: UserProfileSerializer},
    )
    @action(detail=False, methods=["patch"], permission_classes=[IsAuthenticated], url_path="me/partial")
    def me_partial_update(self, request: Request):
        """
        Partially update the current authenticated user's profile (no ID in the URL).
        """
        user = request.user
        profile = get_object_or_404(UserProfile, user_id=user.id, realm_id=user.realm_id)
        serializer = UserProfileUpdateSerializer(profile, data=request.data, partial=True, context={"request": request})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        data = UserProfileSerializer(profile).data
        return Response(data, status=status.HTTP_200_OK)
