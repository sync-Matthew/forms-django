from api.schema import CustomStatelessJWTAuthenticationScheme
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from drf_spectacular.renderers import OpenApiYamlRenderer
from drf_spectacular.views import (
    SpectacularSwaggerView,
    SpectacularAPIView,
    SpectacularRedocView,
)


@method_decorator(login_required, name="dispatch")
class CustomSpectacularSwaggerView(SpectacularSwaggerView):
    pass


@method_decorator(login_required, name="dispatch")
class CustomSpectacularAPIView(SpectacularAPIView):
    renderer_classes = [OpenApiYamlRenderer]

    def finalize_response(self, request, response, *args, **kwargs):
        response = super().finalize_response(request, response, *args, **kwargs)
        response["Content-Disposition"] = 'attachment; filename="forms-django.yaml"'
        return response


@method_decorator(login_required, name="dispatch")
class CustomSpectacularRedocView(SpectacularRedocView):
    pass
