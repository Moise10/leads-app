from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
  pass


class Agent(models.Model):
  user = models.ForeignKey(User,on_delete=models.CASCADE)

  def __str__(self):
    return self.user.email


class Lead(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    age = models.IntegerField(null=True, default=0)
    agent = models.ForeignKey("Agent", on_delete=models.CASCADE)

    def __str__(self):
      return self.first_name
