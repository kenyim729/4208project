from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from blog.models import Post

class Comment(models.Model):
    title = models.ForeignKey(Post, on_delete=models.CASCADE)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.content

