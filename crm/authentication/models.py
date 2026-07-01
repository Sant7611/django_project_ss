from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    # OneToOneField = ForeignKey + UNIQUE constraint
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,      # Delete Profile when User is deleted
        related_name='profile'         # Access profile from User using user.profile
    )
 
    bio = models.TextField(blank=True)

    birth_date = models.DateField(
        null=True,
        blank=True
    )
    phone = models.CharField(
        max_length=20,
        blank=True
    )
 
    def __str__(self):
        return f"Profile of {self.user.username}"
