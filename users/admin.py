from django.contrib import admin
from django.contrib.auth import get_user_model
# from django.contrib.auth.admin import UserAdmin
from .models import User, Role, UserRole, Profile, Permissions

User = get_user_model()

# Register your models here.
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff', 'oauth_provider', 'oauth_uid')  # Include your custom fields here
    search_fields = ('username', 'email')
    model = User

admin.site.register(User, CustomUserAdmin)
admin.site.register(Role)
admin.site.register(Profile)
admin.site.register(Permissions)
admin.site.register(UserRole)