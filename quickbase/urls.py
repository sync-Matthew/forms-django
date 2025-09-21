from django.urls import path
from .views import QuickbaseListAppsView, QuickbaseListTablesView, QuickbaseListFieldsView

urlpatterns = [
    path("quickbase/apps", QuickbaseListAppsView.as_view(), name="quickbase_apps"),
    path("quickbase/tables", QuickbaseListTablesView.as_view(), name="quickbase_tables"),
    path("quickbase/fields", QuickbaseListFieldsView.as_view(), name="quickbase_fields"),
]