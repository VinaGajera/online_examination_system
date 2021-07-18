from django.db import models

# Create your models here.
class signup(models.Model):
    firstname=models.CharField(max_length=20)
    lastname=models.CharField(max_length=20)
    email=models.CharField(max_length=20)
    contact=models.PositiveIntegerField(max_length=12)
    city=models.CharField(max_length=40)
    username=models.CharField(max_length=20)
    password=models.CharField(max_length=8)    
    profile_photo=models.ImageField(upload_to='profile_pic/')
    

