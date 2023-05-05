from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Notes(models.Model):

    title = models.CharField(max_length=100)
    note = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)

    def __str__(self):
        return self.title


class Trash(models.Model):

    title = models.CharField(max_length=100)
    note = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)

    def __str__(self):
        return self.title
    

