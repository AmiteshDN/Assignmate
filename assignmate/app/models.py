from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth import get_user_model

User = get_user_model()     # This ensures that custom user model is used

# Create your models here.
class Assignment(models.Model):
    title = models.CharField(max_length=255,  help_text="Enter title of the assignment")
    description = models.TextField(help_text="Provide a detailed description of the assignment")
    posted_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="assignments_posted")
    assigned_to = models.ForeignKey(User, on_delete=models.SET_NULL,
                                    null=True,
                                    blank=True,
                                    related_name="assignments_assigned")
    due_date = models.DateTimeField(help_text="Enter due date for assignment submission")
    priority = models.IntegerField(
                    default=1,
                    validators=[MinValueValidator(1), MaxValueValidator(10)],
                    help_text="On a scale of 10"
                    )
    assignment_files = models.FileField(upload_to='assignments/files/',
                                        null=True,
                                        blank=True,
                                        help_text="Upload the related files")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title} (Priority: {self.priority})"
  
    class Meta:
        verbose_name = "Assignment"
        verbose_name_plural = "Assignments"
    