# articles/models.py
from django.conf import settings
from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse

class Post(models.Model):
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.body

    def get_absolute_url(self):
        return reverse('feed_list')

class Comment(models.Model):
    post = models.ForeignKey(
        Post, 
        on_delete=models.CASCADE,
        related_name='comments',
        )
    comment = models.CharField(max_length=140)
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,

    )

    def __str__(self):
        return self.comment

    def get_absolute_url(self):
        return reverse('feed_list')