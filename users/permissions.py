from rest_framework.permissions import BasePermission, SAFE_METHODS


class HasUserPermissions(BasePermission):
    """
    Enforce Auth0 "permissions" claim for read vs write access.
    Expects permissions like "read:users" and "write:users".
    """

    read_permission = "read:users"
    write_permission = "write:users"

    def has_permission(self, request, view):
        permissions = []
        auth = getattr(request, "auth", None)
        if isinstance(auth, dict):
            permissions = auth.get("permissions", []) or []
        elif hasattr(request, "user") and hasattr(request.user, "auth0_permissions"):
            permissions = request.user.auth0_permissions or []

        if request.method in SAFE_METHODS:
            return self.read_permission in permissions
        return self.write_permission in permissions
