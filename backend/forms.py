from django import forms
from . import models
import re

# Forms for user login
class LoginForm(forms.Form):
    username = forms.CharField(max_length=150)
    password = forms.CharField(widget=forms.PasswordInput)

# Forms for user register
class RegisterForm(forms.Form):
    username = forms.CharField(max_length=150)
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)

    def clean_password(self):
        password = self.cleaned_data['password']

        # Check password length: between 8 and 14 characters
        if not (8 <= len(password) <= 14):
            raise forms.ValidationError("Password must be between 8 and 14 characters long.")

        # Must contain at least one uppercase letter
        if not re.search(r'[A-Z]', password):
            raise forms.ValidationError("Password must contain at least one uppercase letter.")

        # Must contain at least one digit
        if not re.search(r'\d', password):
            raise forms.ValidationError("Password must contain at least one number.")

        # Must contain at least one special character
        if not re.search(r'[!@#$%^&*(),.?":{}|<>_\[\]\\/\-+=]', password):
            raise forms.ValidationError("Password must contain at least one special character.")

        return password

# Forms for notes
class NoteForm(forms.ModelForm):

    class Meta:
        model = models.Note
        fields = ['title', 'content']

