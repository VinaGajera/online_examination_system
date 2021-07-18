from django.contrib import admin
from django.urls import path,include
from Student import views

urlpatterns = [
    path('',views.signup,name="signup")
    

]