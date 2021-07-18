from django.shortcuts import render
from .forms import signupModel
from Student.models import signup

# Create your views here.

def signup(request):
    return render(request,'signup.html')
    # if request.method=='POST':
    #     signupreq=signupModel(request.POST)
    #     if signupreq.is_valid();
    #         signupreq.save()
    #         print

    
