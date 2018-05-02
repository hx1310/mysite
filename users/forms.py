from django.contrib.auth.forms import UserCreationForm
from .models import User

class RigisterForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ("username","email")

