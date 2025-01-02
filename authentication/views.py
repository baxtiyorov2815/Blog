from django.shortcuts import get_object_or_404, render, redirect
from django.views import View
from .forms import FollowUserForm, RegistrationForm, UserProfileFirstForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from .models import UserProfile, UserFollowersModel
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin

class RegisterPageView(View):
    def get(self, request):
        form = RegistrationForm()
        context = {'form': form}
        return render(request=request,
                      template_name='registration/register.html',
                      context=context)
    
    def post(self, request):
        try:
            username = request.POST.get("username")
            email = request.POST.get("email")
            password1 = request.POST.get("password1")
            password2 = request.POST.get("password2")
            if password1 == password2:
                messages.add_message(request, messages.SUCCESS, 'User successfully registred!')
                user = User.objects.create_user(username=username,
                                                email=email,
                                                password=password1)
                user.save()
                userprofile = UserProfile(user=user)
                userprofile.save()
                login(request=request,
                    user=user)
                return redirect('home')
            else:
                messages.add_message(request, messages.ERROR, 'Password didnt match!!!')
                return render(request=request,
                            template_name='registration/register.html',
                            )
        except:
            messages.add_message(request, messages.ERROR, 'Something went wrong')
            return render(request=request,
                            template_name='registration/register.html',
                            )
        
class BanUserView(View):
    def get(self, request, pk):
        user = User.objects.filter(id=pk).first()
        user.is_active = False
        user.save()
        return redirect('home')

# class LoginPageView(View):
#     def get(self, request):
#         return render(request=request,
#                       template_name='registration/login.html')
    
#     def post(self, request):
#         form = RegistrationForm(request.POST)
#         if form.is_valid():
#             user = form.save()
#             login(request, user)
#             return redirect('home')
#         else:
#             messages.add_message(request, messages.ERROR, "Somthing went wrong please try again!")
#             return redirect('home')

class LoginPageView(View):
    def get(self, request):
        form = AuthenticationForm()
        return render(request, 'registration/login.html', {'form': form})      
    def post(self, request):
            form = AuthenticationForm(data=request.POST)
            if form.is_valid():
                username = form.cleaned_data.get('username')
                password = form.cleaned_data.get('password')
                user = authenticate(request, username=username, password=password)
                if user is not None:
                    login(request, user)
                    return redirect('home')
                else:
                    messages.error(request, "Invalid username or password!")
            else:
                messages.error(request, "Invalid login details. Please try again!")
            
            return render(request, 'registration/login.html', {'form': form})

class LogoutPageView(View):
    def get(self, request):
        user = request.user
        logout(request)
        return redirect('home')
    
class UserProfileView(View):
    def get(self, request, username, *args, **kwargs):
        user = User.objects.get(username=username)
        userprofile = UserProfile.objects.filter(user=user)
        print(userprofile[0].followers)
        followed = userprofile[0].followers.filter(id=request.user.id).exists()
        context = {
            "userprofile": userprofile[0],
            "followed": followed
        }
        return render(request, 'user/user_profile.html', context=context)
    def post(self, request, *args, **kwargs):
        pass

class FollowUserView(LoginRequiredMixin, View):
    def post(self, request, username, *args, **kwargs):
        user_to_follow = get_object_or_404(User, username=username)
        user_profile_to_follow = get_object_or_404(UserProfile, user=user_to_follow)

        if user_to_follow != request.user:
            user_profile_to_follow.followers.add(request.user)
            messages.success(request, f'You are now following {user_to_follow.username}.')
        else:
            messages.error(request, "You cannot follow yourself!")

        return redirect('userprofile', username=username)


class UnfollowUserView(LoginRequiredMixin, View):
    def post(self, request, username, *args, **kwargs):
        user_to_unfollow = get_object_or_404(User, username=username)
        user_profile_to_unfollow = get_object_or_404(UserProfile, user=user_to_unfollow)

        if user_to_unfollow != request.user:
            user_profile_to_unfollow.followers.remove(request.user)
            messages.success(request, f'You have unfollowed {user_to_unfollow.username}.')
        else:
            messages.error(request, "You cannot unfollow yourself!")

        return redirect('userprofile', username=username)