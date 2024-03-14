from typing import Any
from django.forms.models import BaseModelForm
from django.shortcuts import render
from django.views.generic.edit import CreateView
from .models import User
from .forms import hrRegistrationForm, employeeRegistrationForm
#import settings.py
from django.conf import settings
#send_mail is built-in function in django
from django.core.mail import send_mail
from django.http import HttpRequest, HttpResponse
from django.contrib.auth.views import LoginView
from django.views.generic import ListView
from employee.models import UserDetail

# Create your views here.
class hrRegisterView(CreateView):
    template_name = 'user/hr_register.html'
    model = User
    form_class = hrRegistrationForm
    success_url = '/user/login/'
    
    def form_valid(self, form):
        email = form.cleaned_data.get('email')
        #print("email....",email)
        if sendMail(email):
            print("Mail sent successfully")
            return super().form_valid(form)
        else:
            return super().form_valid(form)
            


class employeeRegisterView(CreateView):
    template_name = 'user/employee_register.html'
    model = User
    form_class = employeeRegistrationForm
    success_url = 'user/login/'    



def sendMail(request):
    subject = 'Welcome to hrportal'
    message = 'Hope you are enjoying your Django Tutorials'
    #recepientList = ["samir.vithlani83955@gmail.com"]
    recepientList = ['vinit1222003@gmail.com']
    EMAIL_FROM = settings.EMAIL_HOST_USER
    send_mail(subject,message, EMAIL_FROM, recepientList)
    #attach file
    #html
    return True
    
class UserLoginView(LoginView): 
    template_name = 'user/login.html'
    model = User
    
    
    def get_redirect_url(self):
        if self.request.user.is_authenticated:
            if self.request.user.is_hr:
                return '/user/hr_dashboard/'
            else:
                return '/user/employee_dashboard/'
            
class hrDashboardView(ListView):
    
    def get(self, request, *args, **kwargs):
        #logic to get all the projects
    
       userDetails = UserDetail.objects.all()
       return render(request, 'user/hr_dashboard.html',{
         "userdetails":userDetails
     })

    
    template_name = 'user/hr_dashboard.html'

class employeeDashboardView(ListView):
    def get(self, request, *args, **kwargs):
        #logic to get all the projects
        return render(request, 'user/employee_dashboard.html')
    
    template_name = 'user/employee_dashboard.html'    
       