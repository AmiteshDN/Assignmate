from django.urls import path, include
from . import views
from app.views import index as app_index
from rest_framework import routers

urlpatterns = [
    
]

urlpatterns += [path('', app_index, name='app_index')]