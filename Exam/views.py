from django.shortcuts import render,HttpResponse
from datetime import datetime
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request,'index.html')

# def about(request):
#     return render(request,'about.html')

# def purpose(request):
#      return render(request,'purpose.html')

# def contact(request):   
#    if request.method =='POST':
#       name=request.POST.get('username')
#       email_id=request.POST.get('email')
#       contact_no=request.POST.get('phone')
#       message=request.POST.get('message')
#       contact = Contact (name=name,email_id=email_id,contact_no=contact_no,message=message,datetime=datetime.today())
#       contact.save()
#       messages.success(request, 'Your message is sent to admin we can contact you in 24 hours.')
#    return render(request,'contact.html')

   




