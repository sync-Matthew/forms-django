from drf_spectacular.utils import OpenApiParameter
from drf_spectacular.types import OpenApiTypes

class UserProfileParameter(OpenApiParameter):
    def __init__(self):
        super().__init__(
            name="id",
            type=OpenApiTypes.UUID,
            location=OpenApiParameter.PATH,
            description="User Profile ID",
        )
