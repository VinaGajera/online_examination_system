from Student.views import signup
from django.shortcuts import render ,reverse
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth import logout
from django.shortcuts import redirect
from admin.models import *
from django.contrib import messages

# Create your views here.

def index(request):  
    if not request.user.is_authenticated:
        return redirect('admin:admin_login')
    return render(request, 'admin/index.html') 

def about(request):
    return render(request,'about.html')

def purpose(request):
    return render(request,'purpose.html')

def admin_login(request):
    error = ""
    if request.method == "POST":
        a_email = request.POST['a_email']
        a_pass = request.POST['a_pass']
        user = authenticate(request, username=a_email, password=a_pass)
        if user is not None:
            print("ADDDDDDD")
            try:
                login(request, user)
                print("Loggggginnn")
                return redirect("admin:index")
            except Exception as e:
                error = e
        else:
            error = "yes"
    context = {"error": error}
    return render(request, "admin/admin_login.html", context)  

def add_course(request):
    if not request.user.is_authenticated:
        return redirect('admin:admin_login')
    if request.method == "POST":
        course_name= request.POST['course_name']
        number_of_question=request.POST['number_of_question']
        total_marks=request.POST['total_marks']
        passing_marks=request.POST['passing_marks']
        try:
            course = Course.objects.create(course_name=course_name, number_of_question=number_of_question,total_marks=total_marks,passing_marks=passing_marks)
            print('couse_iddd : ',course.id)
            return redirect(reverse('admin:add_ques', kwargs={'id': course.id, 'num_of_ques': course.number_of_question,'total_mark':course.total_marks}))
        except Exception as e:
            print('error',e)
    return render(request, "admin/add_course.html")

def add_ques(request,id,num_of_ques,total_mark):
    if not request.user.is_authenticated:
        return redirect('admin:admin_login')
    print('night_owl : ',id,num_of_ques,total_mark)
    num_of_ques=int(num_of_ques)
    print('BADIII : ',type(num_of_ques))
    if num_of_ques >= 1:
        if request.method =="POST":
            mark= request.POST['mark']
            question = request.POST['question']
            option1 =request.POST['option1']
            option2 =request.POST['option2']
            option3 =request.POST['option3']
            answer = ""
            c_answer = request.POST['c_answer']
            c_answer = int(c_answer)
            if c_answer == 1:
                answer = option1
                print("inside_first_click")
            elif c_answer == 2:
                answer = option2
            elif c_answer == 3:
                answer = option3
            else:
                answer = "Blank"
            print("c_answer : ",c_answer)
            print("Correct_anser : ",answer)
            if answer != "Blank":
                num_of_ques = num_of_ques - 1
                try:
                    ques=Question.objects.create(marks=mark,question=question,option1=option1,option2=option2,option3=option3,answer=answer,course_id=id)
                    return redirect(reverse('admin:add_ques', kwargs={'id': id, 'num_of_ques': num_of_ques,'total_mark':total_mark}))
                    #return render(request,"admin/add_question.html",{'cid':id,'num_of_ques':num_of_ques,'total_mark':total_mark})
                except Exception as e:
                    print("Error",e)
    else:
        print("Final Question")
        return redirect('admin:index')
    return render(request, "admin/add_question.html",{'cid':id,'num_of_ques':num_of_ques,'total_mark':total_mark})

def delete_student_view(request,pk):
    student=Signup.objects.get(id=pk)
    print('delete student',pk)
    student.delete()
    return redirect('admin:admin_view_student')

def delete_contact_view(request,pk):
    contact=Contact.objects.get(id=pk)
    print('delete Contact',pk)
    contact.delete()
    return redirect('admin:contact_view')

def admin_student_view(request):
    dict={
    'total_student':Signup.objects.all().count(),
    }
    return render(request,'admin/admin_student.html',context=dict)

def admin_view_student_view(request):
    students= Signup.objects.all()
    return render(request,'admin/admin_view_student.html',{'students':students})

def admin_view_student_marks_view(request):
    students= Signup.objects.all()
    return render(request,'admin/admin_view_student_marks.html',{'students':students})

def admin_view_marks_view(request,pk):
    courses = Course.objects.all()
    response =  render(request,'admin/admin_view_marks.html',{'courses':courses})
    response.set_cookie('student_id',str(pk))
    return response

def admin_check_marks_view(request,pk):
    course = Course.objects.get(id=pk)
    student_id = request.COOKIES.get('student_id')
    student= Signup.objects.get(id=student_id)
    results= Result.objects.all().filter(exam=course).filter(student=student)
    return render(request,'admin/admin_check_marks.html',{'results':results})

def contact_view(request):
    dict={
    'contact':Contact.objects.all()
    }
    return render(request,'admin/contact_view.html',context=dict)

def admin_logout(request):
    if not request.user.is_authenticated:
        return redirect('admin:admin_login')
    logout(request)
    return redirect("admin:admin_login") 