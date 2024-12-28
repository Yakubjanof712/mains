from django.db import models
from django.contrib.auth.models import User
class DataModel(models.Model):
    name = models.CharField(max_length=100)

def my_function():
    from .models import DataModel
class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


