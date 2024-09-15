from django.contrib import admin
from .models import Assignment, AssignmentRequest


# Register your models here.
admin.site.register(Assignment)
admin.site.register(AssignmentRequest)
