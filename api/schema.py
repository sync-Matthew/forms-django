from drf_spectacular.contrib.rest_framework_simplejwt import SimpleJWTScheme
from api.authentication import CustomStatelessJWTAuthentication


class CustomStatelessJWTAuthenticationScheme(SimpleJWTScheme):
    target_class = CustomStatelessJWTAuthentication
    name = "Chatbot Stateless JWT Authentication"
