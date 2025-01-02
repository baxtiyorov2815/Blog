from django.urls import path
from .views import RegisterPageView, BanUserView, LoginPageView, LogoutPageView, UserProfileView, FollowUserView, UnfollowUserView

urlpatterns = [
    path('login/', LoginPageView.as_view(), name='login'),
    path('register/', RegisterPageView.as_view(), name='register'),
    path('logout/', LogoutPageView.as_view(), name='logout'),
    path('banuser/<int:pk>/', BanUserView.as_view(), name='ban'),
    path('user/<str:username>/', UserProfileView.as_view(), name='userprofile'),
    path('follow/<str:username>/', FollowUserView.as_view(), name='follow_user'),
    path('unfollow/<str:username>/', UnfollowUserView.as_view(), name='unfollow_user'),
    # path('follow/<int:pk>', FollowUserView.as_view(), name='follow')
]