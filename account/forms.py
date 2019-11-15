from django import forms
from .models import User
# from django.contrib.auth.models import User

class LoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username','password']

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'student_id', 'major', 'grade', 'phone_number', 'password']