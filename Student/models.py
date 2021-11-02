from django.db import models
# Create your models here.
class Signup(models.Model):
    firstname=models.CharField(max_length=20)
    lastname=models.CharField(max_length=20)
    contact=models.CharField(max_length=12)
    email=models.CharField(max_length=20)
    password=models.CharField(max_length=8)  
    city=models.CharField(max_length=40)
    profile_photo=models.ImageField(upload_to='profile_pic')
    
    def __str__(self):
        return self.email
    

