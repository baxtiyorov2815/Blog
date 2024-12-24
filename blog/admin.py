from django.contrib import admin
from .models import Genre, Post, Comment

@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ['title']

@admin.register(Post)
class GenreAdmin(admin.ModelAdmin):
    list_display = ['title', 'genre', 'created', 'updated']
    fields = ['title', 'desc', 'image', 'genre']

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    pass