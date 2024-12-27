from django import forms
from .models import Genre, Post, Comment

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'desc', 'image', 'genre']

class GenreForm(forms.ModelForm):
    class Meta:
        model = Genre
        fields = "__all__"