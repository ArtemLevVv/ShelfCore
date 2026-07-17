from django.contrib.auth.forms import UserCreationForm
from .models import User

class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = [
            'username',
            'password1',
            'password2',
            'email'
        ] 
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["username"].help_text = ""
        self.fields["password1"].help_text = ""
        self.fields["password2"].help_text = ""