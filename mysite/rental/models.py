from django.db import models

# Create your models here.


class Friend(models.Model):
    name = models.CharField(max_length=100)

class Belonging(models.Model):
    name = models.CharField(max_length=100)

class Borrowed(models.Model):
    what = models.ForeignKey(Belonging, on_delete=models.CASCADE,related_name='borrowedbelonging',null=True,blank=True)
    to_who = models.ForeignKey(Friend, on_delete=models.CASCADE,related_name='borrowedfriend',null=True,blank=True)
    when = models.DateTimeField(auto_now_add=True)
    returned = models.DateTimeField(null=True, blank=True)

class Category(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=100, blank=False)

class Movie(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=100, blank=False)
    category = models.ForeignKey(Category,related_name='movies',
                               on_delete=models.CASCADE,
                               blank=True,
                               null=True)
