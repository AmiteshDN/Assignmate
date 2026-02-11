import json
import os
from dotenv import load_dotenv, find_dotenv
from authlib.integrations.django_oauth2 import ResourceProtector
from django.http import JsonResponse
from . import validator
from django.shortcuts import render, redirect
from django.conf import settings
from django.urls import reverse
from urllib.parse import urlencode
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .permissions import HasUserPermissions
from .serializers import UserSerializer
from django.contrib.auth import get_user_model
from .authentication import Auth0Authentication


User = get_user_model()
ENV_FILE = find_dotenv()
if ENV_FILE:
    load_dotenv(ENV_FILE)

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    authentication_classes = [Auth0Authentication]
    permission_classes = [IsAuthenticated, HasUserPermissions]









