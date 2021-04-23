from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth import get_user_model


# Create your models here.

class CustomUser(AbstractUser):
    age = models.PositiveIntegerField(null=True, blank=True)
    location = models.CharField(max_length=255)
    bio = models.TextField(null=True)


class Following(models.Model):
    user_id = models.ForeignKey(CustomUser, related_name="following", on_delete=models.CASCADE, null=True, blank = True)
    following_user_id = models.ForeignKey(CustomUser, related_name="followers", on_delete=models.CASCADE, null=True, blank = True)

    class Meta:
        unique_together = ["user_id", "following_user_id"]

    def __str__(self):
        return f"{self.user_id} follows {self.following_user_id}"
