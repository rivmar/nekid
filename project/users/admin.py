from django.contrib import admin
from .models import Users
from .forms import UserCreationForm

class UsersAdmin(admin.ModelAdmin):
    form = UserCreationForm

admin.site.register(Users, UsersAdmin)