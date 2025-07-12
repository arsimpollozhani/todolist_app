"""
URL configuration for mysite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from register import views as v
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),  # admin
    path("register/", v.register, name="register"),  # app: register
    path('', include("main.urls")), # app: main

    # Login view
    path("register/login/", auth_views.LoginView.as_view(template_name='register/login.html'), name="login"), # custom

    # Logout with redirect to login page after logout
    path("logout/", auth_views.LogoutView.as_view(next_page="login"), name="logout"),  # custom

    path("account/", v.account, name="account"),  # app: register

    path('', include("django.contrib.auth.urls")), # for authentication

    
    
]
