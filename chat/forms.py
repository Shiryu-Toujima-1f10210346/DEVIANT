from django import forms
from .models import Comment, Post
from django.contrib.auth.models import User
class AccountForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username','email',"password")
class CommentForm(forms.ModelForm):
    class Meta:
        #labelを変更
        labels = {
            'text': '',
        }
        model = Comment
        fields = ('text',)