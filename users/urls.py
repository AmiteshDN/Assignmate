from django.urls import path
from . import views
from app.views import index as app_index

urlpatterns = [
    path("api/register-role/", views.RegisterRoleView.as_view(), name="register_role"),
]

urlpatterns += [path('', app_index, name='app_index')]
