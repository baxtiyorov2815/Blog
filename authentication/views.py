from django.shortcuts import render, redirect
from django.views import View
from .forms import RegistrationForm, UserForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.messages import constants
from django.contrib import messages


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