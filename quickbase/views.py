from .client import get_quickbase_client
from .serializers import (
    QuickbaseAppSerializer,
    QuickbaseTableSerializer,
)
from profiles.models import UserProfile
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response


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


class QuickbaseListTablesView(APIView):
    """
    View to list all tables in a Quickbase app.

    * Requires sign-in.
    """
    permission_classes = [IsAuthenticated]
    serializer_class = QuickbaseTableSerializer

    def get(self, request, app_id: str):
        """
        Return a list of all tables in the specified app.
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
            tables = client.list_tables(app_id=app_id)
            serializer = QuickbaseTableSerializer(tables, many=True)
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response(data={"detail": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class QuickbaseListFieldsView(APIView):
    pass