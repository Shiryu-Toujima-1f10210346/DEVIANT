from django import forms
from .models import Account
from django.contrib.auth.models import User
class AccountForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username','email',"password")