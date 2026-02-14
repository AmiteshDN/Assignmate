from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from .permissions import HasUserPermissions
from .serializers import UserSerializer
from django.contrib.auth import get_user_model
from .authentication import Auth0Authentication
from .models import Role, UserRole


User = get_user_model()

class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that allows users to be viewed.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    authentication_classes = [Auth0Authentication]
    permission_classes = [IsAuthenticated, HasUserPermissions]


class RegisterRoleView(APIView):
    """
    Register the authenticated user with a role (student or teacher).
    Expects JSON body: {"role": "student"} or {"role": "teacher"}
    """
    authentication_classes = [Auth0Authentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):
        role_name = (request.data.get("role") or "").strip().lower()
        if role_name not in {"student", "tutor"}:
            return Response(
                {"detail": "Role must be 'student' or 'teacher'."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        role = Role.objects.filter(name__iexact=role_name).first()
        if not role:
            return Response(
                {"detail": f"Role '{role_name}' not found."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        user = request.user
        if not user.email:
            email = request.data.get("email", "")
            if email:
                user.email = email
                user.save(update_fields=["email"])

        user_role, created = UserRole.objects.get_or_create(user=user, role=role)
        return Response(
            {
                "user": user.username,
                "role": role.name,
                "created": created,
            },
            status=status.HTTP_201_CREATED if created else status.HTTP_200_OK,
        )









