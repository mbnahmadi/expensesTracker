from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


# class CustomUser(AbstractUser):
#     first_name = models.CharField(max_length=20)
#     last_name = models.CharField(max_length=20)
#     email = models.EmailField(unique=True)
#     username = models.CharField(max_length=10 , unique=True)

#     def __str__(self):
#         return self.username

