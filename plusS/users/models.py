from django.db import models
from pyparsing import empty

class User(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    email = models.EmailField(max_length=254, unique=True, blank=False)
    username = models.CharField(max_length=100)

    class Meta:
        ordering = ['created']