from django.contrib import admin
from django.contrib.auth.models import Group
from .models import Users

class UsersAdmin(admin.ModelAdmin):
    pass

admin.site.register(Users, UsersAdmin)
admin.site.unregister(Group)