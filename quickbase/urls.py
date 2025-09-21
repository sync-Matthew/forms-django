from django.urls import path
from .views import QuickbaseListAppsView, QuickbaseListTablesView, QuickbaseListFieldsView

urlpatterns = [
    path("quickbase/apps", QuickbaseListAppsView.as_view(), name="quickbase_apps"),
    path("quickbase/apps/<str:app_id>/tables", QuickbaseListTablesView.as_view(), name="quickbase_tables"),
    path("quickbase/tables/<str:table_id>/fields", QuickbaseListFieldsView.as_view(), name="quickbase_fields"),
]