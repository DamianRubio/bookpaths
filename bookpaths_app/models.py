from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass

class Category(models.Model):
    name = models.CharField(max_length=50, primary_key=True)

    def __str__(self):
        return f'Category: {self.name}'