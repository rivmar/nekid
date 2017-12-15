from django.forms import ModelForm
from .models import Users

class UserCreationForm(ModelForm):
    class Meta:
        model = Users
        exclude = 'password', 'groups', 'user_permissions'