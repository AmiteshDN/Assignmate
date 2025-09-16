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
    id = models.CharField(max_length=10, 
                          primary_key=True, 
                          unique=True, 
                          blank=False,
                          help_text="Start with ROL and add a number. eg: ROL101")
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return f"{self.name}"
    

# model for tagging role to the user
class UserRole(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="roles")
    role = models.ForeignKey(Role, on_delete=models.CASCADE, related_name="users")

    
    class Meta:
        unique_together = ('user', 'role')
    

    def __str__(self):
        return f"{self.user} - {self.role.name}"



# Profile model
class Profile(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    bio = models.TextField(help_text="Enter bio")
    dob = models.DateField()
    # profile_picture = models.URLField()
    
    def __str__(self):
        return f"{self.user_id}"


# Permission model
class Permissions(models.Model):
    id = models.CharField(primary_key=True,
                          unique=True,
                          blank=False,
                          help_text="Enter an id starting with PERM and 3 digit number eg:PERM101",
                          null=False,
                          )
    name = models.CharField(unique=True, blank=False, null=False)

    class Meta:
        db_table = 'permissions' 
        verbose_name = 'Permission'
        verbose_name_plural = 'Permissions'

    def __str__(self):
        return f"{self.id}"