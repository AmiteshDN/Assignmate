from django.shortcuts import render, redirect
from django.http import HttpResponse
import json

# Create your views here.
def index(request):
    return render(
        request,
        "assignmate/index.html",
        context={
            "session": request.session.get("user"),
            "pretty": json.dumps(request.session.get("user"), indent=4),
        },
    )


# API viewset stubs for assignments (no logic inside methods)
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Assignment
from .serializers import AssignmentSerializer
from users.authentication import Auth0Authentication


class AssignmentViewSet(viewsets.ModelViewSet):
    """Assignment CRUD API stubs: methods intentionally empty.

    These are placeholders — no internal logic is implemented.
    """

    queryset = Assignment.objects.all()
    serializer_class = AssignmentSerializer
    authentication_classes = [Auth0Authentication]
    permission_classes = [IsAuthenticated]

    def list(self, request, *args, **kwargs):
        pass

    def retrieve(self, request, *args, **kwargs):
        pass

    def create(self, request, *args, **kwargs):
        pass

    def update(self, request, *args, **kwargs):
        pass

    def partial_update(self, request, *args, **kwargs):
        pass

    def destroy(self, request, *args, **kwargs):
        pass

    def perform_create(self, serializer):
        pass
