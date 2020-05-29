"""Fraudapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path,include
from .import views

app_name="fraud" 

urlpatterns = [
    path('',views.index,name="index"),
    path('student',views.home,name="home"),
    path('reg',views.reg,name="reg"),
    path('template',views.temp,name="temp"),
    path('login',views.login,name="login"),
    path('user_chk',views.user_chk,name="user_chk"),
    path('register',views.register,name="register"),
    path('forgot_pswd',views.forgot_pswd,name="forgot_pswd.html"),
    path('loadData',views.loadData,name="loadData"),
    path('reviewApp',views.reviewApp,name="reviewApp"),
    path('sendreview',views.sendreview,name="sendreview"),
    path('seereview',views.seereview,name="seereview"),
    path('saveUser',views.saveUser,name="saveUser"),
    

]

