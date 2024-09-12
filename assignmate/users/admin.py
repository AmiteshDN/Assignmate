from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

# Register your models here.
class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff')  # Include your custom fields here
    search_fields = ('username', 'email')
    model = User

admin.site.register(User, CustomUserAdmin)