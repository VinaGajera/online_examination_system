from django.urls import path
from Student import views
from django.conf import settings
from django.conf.urls.static import static

app_name = "student"

urlpatterns = [
    path('',views.index,name="index"),
    path('signup',views.signup,name="signup"),
    path('about',views.about,name="about"),
    path('purpose',views.purpose,name="purpose"),
    path('contact',views.contact,name="contact"),    
    path('signin',views.signin,name="signin"),
    path('studentdeshboard',views.studentdeshboard,name="studentdeshboard"),
    path('stud_feedback/',views.feedback,name="stud_feedback"),
    path('student_exam/',views.student_exam,name="student_exam"),
    path('take_exam/<id>',views.take_exam,name="take_exam"),
    path('start_exam/<id>',views.start_exam,name="start_exam"),
    path('student_marks/',views.student_marks,name="student_marks"),
    path('view_result', views.view_result_view,name='view_result'),
    path('check_marks/<int:pk>',views.check_marks,name='check_marks'),
    path('stud_logout/',views.stud_logout,name="stud_logout"),
    

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)