from .client import get_quickbase_client
from .serializers import (
    QuickbaseAppSerializer,
    QuickbaseTableSerializer,
    QuickbaseFieldSerializer,
)
from drf_spectacular.utils import extend_schema, extend_schema_view, OpenApiParameter
from profiles.models import UserProfile
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response

@extend_schema_view(
    get=extend_schema(
        responses={200: QuickbaseAppSerializer(many=True)}
    )
)
class QuickbaseListAppsView(APIView):
    """
    View to list all of the users' Quickbase apps.

    * Requires sign-in.
    """
    permission_classes = [IsAuthenticated]
    serializer_class = QuickbaseAppSerializer

    def get(self, request):
        """
        Return a list of all apps.
        """
        try:
            profile = UserProfile.objects.get(user_id=request.user.id, realm_id=request.user.realm_id)
        except UserProfile.DoesNotExist:
            return Response(data={"detail": "User profile not found."}, status=status.HTTP_404_NOT_FOUND)

        try:
            client = get_quickbase_client(
                realm=profile.realm,
                user_token=profile.user_token,
            )
            apps = client.list_apps(profile=profile)
            serializer = QuickbaseAppSerializer(apps, many=True)
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response(data={"detail": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@extend_schema_view(
    get=extend_schema(
        responses={200: QuickbaseTableSerializer(many=True)},
        parameters=[OpenApiParameter(name="app", type=str, location=OpenApiParameter.QUERY, required=True, description="The ID of the Quickbase app to list tables for.")],
    )
)
class QuickbaseListTablesView(APIView):
    """
    View to list all tables in a Quickbase app.

    * Requires sign-in.
    """
    permission_classes = [IsAuthenticated]
    serializer_class = QuickbaseTableSerializer

    def get(self, request):
        """
        Return a list of all tables in the specified app.
        """
        app_id = request.query_params.get("app")

        if not app_id:
            return Response(data={"detail": "app query parameter is required."}, status=status.HTTP_400_BAD_REQUEST)

        try:
            profile = UserProfile.objects.get(user_id=request.user.id, realm_id=request.user.realm_id)
        except UserProfile.DoesNotExist:
            return Response(data={"detail": "User profile not found."}, status=status.HTTP_404_NOT_FOUND)

        try:
            client = get_quickbase_client(
                realm=profile.realm,
                user_token=profile.user_token,
            )
            tables = client.list_tables(app_id=app_id)
            serializer = QuickbaseTableSerializer(tables, many=True)
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response(data={"detail": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@extend_schema_view(
    get=extend_schema(
        responses={200: QuickbaseFieldSerializer(many=True)},
        parameters=[OpenApiParameter(name="table", type=str, location=OpenApiParameter.QUERY, required=True, description="The ID of the Quickbase table to list fields for.")],
    )
)
class QuickbaseListFieldsView(APIView):
    """
    View to list all fields in a Quickbase table.

    * Requires sign-in.
    """
    permission_classes = [IsAuthenticated]
    serializer_class = QuickbaseFieldSerializer

    def get(self, request):
        """
        Return a list of all fields in the specified table.
        """
        table_id = request.query_params.get("table")

        if not table_id:
            return Response(data={"detail": "table query parameter is required."}, status=status.HTTP_400_BAD_REQUEST)

        try:
            profile = UserProfile.objects.get(user_id=request.user.id, realm_id=request.user.realm_id)
        except UserProfile.DoesNotExist:
            return Response(data={"detail": "User profile not found."}, status=status.HTTP_404_NOT_FOUND)

        try:
            client = get_quickbase_client(
                realm=profile.realm,
                user_token=profile.user_token,
            )
            fields = client.list_fields(table_id=table_id)
            serializer = QuickbaseFieldSerializer(fields, many=True)
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response(data={"detail": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
