from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Role, Profile, Permissions

# Register your models here.
class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff', 'oauth_provider', 'oauth_uid')  # Include your custom fields here
    search_fields = ('username', 'email')
    model = User

admin.site.register(User, CustomUserAdmin)

admin.site.register(Role)
admin.site.register(Profile)
admin.site.register(Permissions)