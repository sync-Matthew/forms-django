"""
URL configuration for form_builder project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path, include
from django.contrib import admin
from .views import (
    CustomSpectacularSwaggerView,
    CustomSpectacularAPIView,
    CustomSpectacularRedocView,
)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/docs/", CustomSpectacularSwaggerView.as_view(url_name="schema"), name="swagger-ui"),
    path("api/schema/", CustomSpectacularAPIView.as_view(), name="schema"),
    path("api/schema/redoc/", CustomSpectacularRedocView.as_view(url_name="schema"), name="redoc"),
    path("", include("profiles.urls")),
    path("", include("intake.urls")),
]
