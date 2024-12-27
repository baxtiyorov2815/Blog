from django.shortcuts import render, redirect
from django.views import View
from .forms import RegistrationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User


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
                user = User.objects.create_user(username=username,
                                                email=email,
                                                password=password1)
                user.save()
                login(request=request,
                    user=user)
                return redirect('home')
            else:
                return render(request=request,
                            template_name='registration/register.html',
                            context={"message": "password didnt match"}
                            )
        except:
            return render(request=request,
                            template_name='registration/register.html',
                            context={"message1": "something went wrong please try again"}
                            )


# class LoginPageView(View):
#     def get(self, request):
#         return render(request=request,
#                       template_name='authentication/login.html')
    
#     def post(self, request):
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             user = form.save()
#             authenticate(request, user)
            