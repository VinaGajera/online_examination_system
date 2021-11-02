from django.contrib import admin
from django.urls import path,include
from Exam import views
urlpatterns = [
    path('',views.index,name="index"),
    # path('about',views.about,name="about"),
    # path('purpose',views.purpose,name="purpose"),
    # path('contact',views.contact,name="contact"),
    
    

]