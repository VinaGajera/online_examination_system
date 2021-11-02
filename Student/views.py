from django.shortcuts import render,redirect
from Student.models import *
from admin.models import *
from django.contrib import messages
import datetime
from django.contrib.auth import logout
# Create your views here.

def index(request):
    return render(request,'index.html')

def about(request):
    return render(request,'about.html')

def purpose(request):
     return render(request,'purpose.html')

def contact(request):   
   if request.method =='POST':
      name=request.POST.get('username')
      email_id=request.POST.get('email')
      contact_no=request.POST.get('phone')
      message=request.POST.get('message')
      contact = Contact (name=name,email_id=email_id,contact_no=contact_no,message=message)
      contact.save()
      messages.success(request, 'Your message is sent to admin we can contact you in 24 hours.')
   return render(request,'contact.html')

def signup(request):
    if request.method =='POST':
        firstname=request.POST.get('firstname') 
        lastname=request.POST.get('lastname')   
        contact=request.POST.get('contact') 
        email=request.POST.get('email')        
        password=request.POST.get('password')   
        city=request.POST.get('city')        
        profile_photo=request.FILES['profile_photo']    
        signup = Signup (firstname=firstname,lastname=lastname,contact=contact,email=email,password=password,city=city,profile_photo=profile_photo)
        signup.save()   
        messages.success(request, 'Regiter Successfully!')  
    return render(request,'student/signup.html')    

def signin(request):
    if request.method=='POST':  
        eml=request.POST['email']   
        pas=request.POST['password']    
        user_obj=Signup.objects.filter(email=eml,password=pas)  
        if user_obj:    
            print('Login successfully!')    
            user_data=Signup.objects.get(email=eml,password=pas)
            request.session['e_id']= user_data.id
            u_id = request.session.get('e_id')
            print("My_session_id :",u_id) 
            print('session pass')   
            return redirect('student:studentdeshboard') 
        else:   
            print('Login faild....something went wrong - Try again.')   
    return render(request, 'student/signin.html')   

def studentdeshboard(request):  
    e_id=request.session.get('e_id')   
    print('ddddd :',e_id) 
    print('get session... studentdeshboard page')   
    total_course=Course.objects.all().count()
    total_question=Question.objects.all().count()
    return render(request, 'student/studentdeshboard.html',{'e_id':e_id,'total_course':total_course,'total_question':total_question})


def student_exam(request):  
    e_id=request.session.get('e_id')    
    print('get session... studentdeshboard page')  
    t = Course.objects.all() 
    return render(request, 'student/student_exam.html',{'e_id':e_id,'courses':t})

def take_exam(request,id):
    course=Course.objects.get(id=id)
    total_questions=Question.objects.all().filter(course=course).count()
    questions=Question.objects.all().filter(course=course)
    total_marks=0
    for q in questions:
        total_marks=total_marks + q.marks    
    return render(request,'student/take_exam.html',{'course':course,'total_questions':total_questions,'total_marks':total_marks})

def start_exam(request,id):
    course=Course.objects.get(id=id)
    questions=Question.objects.all().filter(course=course)
    no_of_questions=Question.objects.all().filter(course=course).count()
    if request.method=='POST':
        total_marks=0
        for q in questions:
            print('Answer :',q.answer)
            for key in request.POST:
                print(key)
                value = request.POST[key]
                if value == q.answer:
                    total_marks = total_marks + q.marks
                    print("Badu_Marks: ",total_marks)
                print("First",value)
        result = Result()
        u_id = request.session.get('e_id')
        student = Signup.objects.get(id=u_id)
        result.marks=total_marks
        result.exam=course
        result.student=student
        result.date=datetime.datetime.now()
        result.save()
        return redirect('student:view_result')    
    response= render(request,'student/start_exam.html',{'course':course,'questions':questions})
    response.set_cookie('course_id',course.id)
    return response

# def calculate_marks(request):
#     if request.COOKIES.get('course_id') is not None:
#         course_id = request.COOKIES.get('course_id')
#         course=Course.objects.get(id=course_id)        
#         total_marks=0
#         questions=Question.objects.all().filter(course=course)
#         for i in range(len(questions)):            
#             selected_ans = request.COOKIES.get(str(i+1))
#             actual_answer = questions[i].answer
#             if selected_ans == actual_answer:
#                 total_marks = total_marks + questions[i].marks
#         u_id = request.session.get('e_id')
#         student = Signup.objects.get(id=u_id)
#         result = Result()
#         result.marks=total_marks
#         result.exam=course
#         result.student=student
#         result.save()
#         return redirect('student:view_result')

def view_result_view(request):
    courses=Course.objects.all()
    return render(request,'student/view_result.html',{'courses':courses})

def check_marks(request,pk):
    course=Course.objects.get(id=pk)
    u_id = request.session.get('e_id')
    print("student_iddddd:",u_id)
    student = Signup.objects.get(id=u_id)
    results=Result.objects.all().filter(exam=course).filter(student=student)
    return render(request,'student/check_marks.html',{'results':results})

def student_marks(request):
    courses=Course.objects.all()
    return render(request,'student/student_marks.html',{'courses':courses})

def feedback(request):  
    return render(request, 'student/stud_feedback.html')    

def stud_logout(request):  
    logout(request)
    try:
        del request.session['e_id'] 
    except Exception as e:
        print(e)
    return redirect('/')
