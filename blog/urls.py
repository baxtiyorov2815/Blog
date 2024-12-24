from django.urls import path
from .views import homepage, aboutpost, deletepost, editpost

urlpatterns = [
    path('', homepage, name='home'),
    path('about/<int:pk>/', aboutpost, name='detail'),
    path('delete/<int:pk>/', deletepost, name='delete'),
    path('edit/<int:pk>/', editpost, name='edit'),
]