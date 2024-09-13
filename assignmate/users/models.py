from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class User(AbstractUser):
    # Abstract user already has basic fields
    # like email, username, first_name etc.,
    profile_image = models.URLField(blank=True, null=True)
    oauth_provider = models.CharField(max_length=50, blank=True, null=True)
    oauth_uid = models.CharField(max_length=255, blank=True, null=True, unique=True)
    # role = models.ForeignKey('Roles', on_delete=models.SET_NULL, null=True, blank=True)

    class Meta:
        db_table = 'user' 
        verbose_name = 'User'
        verbose_name_plural = 'Users'

class Role(models.Model):
    name = models.CharField(max_length=255, unique=True)


