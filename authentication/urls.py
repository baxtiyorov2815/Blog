from django.urls import path
from .views import RegisterPageView, BanUserView, LoginPageView, LogoutPageView

urlpatterns = [
    path('login/', LoginPageView.as_view(), name='login'),
    path('register/', RegisterPageView.as_view(), name='register'),
    path('logout/', LogoutPageView.as_view(), name='logout'),
    path('banuser/<int:pk>', BanUserView.as_view(), name='ban'),
]