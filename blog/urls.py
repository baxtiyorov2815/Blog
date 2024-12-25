from django.urls import path, re_path
from .views import HomePageView, DeletePostView, DetailPostView, EditPostView, CreateNewGenre, CreateNewPost

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('about/<int:pk>/', DetailPostView.as_view(), name='detail'),
    path('delete/<int:pk>/', DeletePostView.as_view(), name='delete'),
    path('edit/<int:pk>/', EditPostView.as_view(), name='edit'),
    path('newgenre/', CreateNewGenre.as_view(), name='newgenre'),
    path('newpost', CreateNewPost.as_view(), name='newpost'),
]