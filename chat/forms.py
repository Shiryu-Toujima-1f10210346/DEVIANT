from django import forms
from .models import Account , Comment, Post
from django.contrib.auth.models import User
class AccountForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username','email',"password")
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('text',)