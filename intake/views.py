from .models import Form
from .serializers import (
    FormCreateSerializer,
    FormReadSerializer,
)
from api.decorators import suppress_django_filter_warning
from api.schema import CustomStatelessJWTAuthenticationScheme
from drf_spectacular.utils import extend_schema_view, extend_schema
from rest_framework import mixins, viewsets, status
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.request import Request


@extend_schema_view(
    list=extend_schema(
        summary="List forms",
    ),
    create=extend_schema(
        summary="Create a form",
    ),
)
class FormViewSet(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    viewsets.GenericViewSet
):
    """
    A ViewSet for viewing and creating forms.
    """
    permission_classes = [IsAuthenticated]

    def get_serializer_class(self):
        if self.action == "create":
            return FormCreateSerializer
        else:
            return FormReadSerializer

    @suppress_django_filter_warning
    def get_queryset(self):
        user = self.request.user
        if user.is_superuser:
            return Form.objects.all()
        return Form.objects.filter(user_id=user.id)
