import json
from urllib.request import urlopen
from authlib.oauth2.rfc7523 import JWTBearerTokenValidator
from authlib.jose.rfc7517 import JsonWebKey


class Auth0JWTBearerTokenValidator(JWTBearerTokenValidator):
    def __init__(self, domain, audience):
        self.issuer = f"https://{domain}/"
        self.audience = audience
        jwks_url = f"https://{domain}/.well-known/jwks.json"
        with urlopen(jwks_url) as response:
            jwks_data = json.load(response)
            
        self.jwks = JsonWebKey.import_key_set(jwks_data)
        super().__init__(self.jwks)

        self.claims_options = {
            "iss": {"essential": True, "value": self.issuer},
            "aud": {"essential": True, "value": self.audience},
            "exp": {"essential": True},
        }