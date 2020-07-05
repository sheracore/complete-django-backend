from django.contrib import admin
from .models import User, UserManager, Friend, Belonging, Borrowed

# Register your models here.

admin.site.register(User)
#admin.site.register(UserManager)
admin.site.register(Friend)
admin.site.register(Belonging)
admin.site.register(Borrowed)
