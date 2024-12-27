from django.shortcuts import render, redirect
from django.views import View
from .forms import RegistrationForm
from django.contrib.auth import authenticate, login, logout


class RegisterPageView(View):
    def get(self, request):
        form = RegistrationForm()
        context = {'form': form}
        return render(request=request,
                      template_name='registration/register.html',
                      context=context)
    
    def post(self, request):
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            
            return redirect('home')
        else:
            form = RegistrationForm()
            context = {'form': form}
            return render(request=request,
                      template_name='registration/register.html',
                      context=context)

# class LoginPageView(View):
#     def get(self, request):
#         return render(request=request,
#                       template_name='authentication/login.html')
    
#     def post(self, request):
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             user = form.save()
#             authenticate(request, user)
            