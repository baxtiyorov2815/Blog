from django.shortcuts import render
from django.views import View

class LoginPageView(View):
    def get(self, reqeust):
        return render(request=reqeust,
                      template_name='authentication/login.html')