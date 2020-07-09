from django.contrib import admin

from . import models
# Register your models here.

admin.site.register(models.Friend)
admin.site.register(models.Belonging)
admin.site.register(models.Borrowed)
admin.site.register(models.Category)
admin.site.register(models.Movie)
