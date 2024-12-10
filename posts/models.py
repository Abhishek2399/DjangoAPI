"""
Class that represents the Post
"""
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    url  = models.URLField()
    poster = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at'] # order the model basis created at


class Vote(models.Model):
    voter = models.ForeignKey(User, on_delete=models.CASCADE)
    post_voted_for = models.ForeignKey(Post, on_delete=models.CASCADE)