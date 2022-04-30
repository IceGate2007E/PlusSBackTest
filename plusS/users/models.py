from django.db import models

class User(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=254, unique=True)

    class Meta:
        ordering = ['created']