from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
# Defining a custom user
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

# Defining role model - [Student, Tutor, Admin]
# Admin role might get added in future
class Role(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return f"{self.name}"
    

# Profile model
class Profile(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    bio = models.TextField(help_text="Enter bio")
    dob = models.DateField()
    # profile_picture = models.URLField()
    
    def __str__(self):
        return f"{self.user_id}"


