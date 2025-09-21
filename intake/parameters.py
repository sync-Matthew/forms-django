from drf_spectacular.utils import OpenApiParameter
from drf_spectacular.types import OpenApiTypes

class DefaultParameter(OpenApiParameter):
    def __init__(self, description: str = "Default ID parameter"):
        super().__init__(
            name="id",
            type=OpenApiTypes,
            location=OpenApiParameter.PATH,
            description=description,
        )
