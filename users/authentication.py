import os
from dotenv import load_dotenv, find_dotenv
from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed
from django.conf import settings
from django.contrib.auth import get_user_model
from .validator import Auth0JWTBearerTokenValidator

ENV_FILE = find_dotenv()
if ENV_FILE:
    load_dotenv(ENV_FILE)

User = get_user_model()


class Auth0Authentication(BaseAuthentication):
    def __init__(self):
        self.validator = Auth0JWTBearerTokenValidator(
            os.environ.get("AUTH0_DOMAIN"),
            os.environ.get("AUTH0_AUDIENCE"),
        )

    def authenticate(self, request):
        auth = request.headers.get("Authorization")
        if not auth or not auth.startswith("Bearer "):
            return None

        token = auth.split(" ")[1]
        try:
            claims = self.validator.authenticate_token(token)
            if not claims:
                raise AuthenticationFailed("Invalid token")

            payload = dict(claims)
            print(payload)
            sub = payload.get("sub")
            email = payload.get("email")

            if not sub:
                raise AuthenticationFailed("Token missing subject (sub) claim")

            # ✅ Create or fetch user
            user, created = User.objects.get_or_create(
                username=sub,
                defaults={"email": email or ""}
            )
            print(user)

            return (user, token)

        except Exception as e:
            raise AuthenticationFailed(f"Token validation failed: {e}")
