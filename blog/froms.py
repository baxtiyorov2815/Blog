from django import forms
from .models import Genre, Post, Comment

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = "__all__"