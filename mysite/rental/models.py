from django.db import models
from django.contrib.auth.models import (
     AbstractBaseUser
)

# Create your models here.

class User (AbstractBaseUser):
    email     = models.EmailField(max_length=255, unique=True)
    full_name = models.CharField(max_length=255, blank=True, null=True)
    active    = models.BooleanField(default=True) # can login
    staff     = models.BooleanField(default=False) # staff user none superuser
    admin     = models.BooleanField(default=False) #superuser


    USERNAME_FIELD = 'email' #username
    # username(USERNAME_FIELD) and password are requierd by default
    REQUIERD_FIELDS = [] # ./manage.py createsuperuser

    def __str__():
        return

    def get_full_name():
        return

    def get_short_name():
        return




class Friend(models.Model):
    name = models.CharField(max_length=100)

class Belonging(models.Model):
    name = models.CharField(max_length=100)

class Borrowed(models.Model):
    what = models.ForeignKey(Belonging, on_delete=models.CASCADE)
    to_who = models.ForeignKey(Friend, on_delete=models.CASCADE)
    when = models.DateTimeField(auto_now_add=True)
    returned = models.DateTimeField(null=True, blank=True)

