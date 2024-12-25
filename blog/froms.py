from django import forms
from .models import Genre, Post, Comment

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = "__all__"

class GenreForm(forms.ModelForm):
    class Meta:
        model = Genre
        fields = "__all__"