from django.contrib.auth.forms import UserCreationForm
from .models import User


class SignupForm(UserCreationForm):
    """
    Create a user with phone and password.
    """
    class Meta:
        model = User
        fields = ('phone', 'email')
