from django.contrib import admin
from django.urls import path, include
from . import views
from django.contrib.auth.views import LoginView,LogoutView

urlpatterns = [
    
    path("hr_register/",views.hrRegisterView.as_view(),name="hr_register"),
    path("login/",views.UserLoginView.as_view(),name="login"),
    path("hr_dashboard/",views.hrDashboardView.as_view(),name="hr_dashboard"),
    # path("developer-register/",views.DeveloperRegisterView.as_view(),name="developer-register"),
    path("developer-dashboard/",views.employeeDashboardView.as_view(),name="employee_dashboard"),
    path("logout/",LogoutView.as_view(next_page = "/user/login"),name="logout"),
    path("sendmail/",views.sendMail,name="sendmail"),
]