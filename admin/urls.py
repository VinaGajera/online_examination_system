from django.urls import path
from admin import views
from django.conf import settings
from django.conf.urls.static import static

app_name = "admin"
urlpatterns = [
    path('',views.index,name="index"),
    path('contact_view',views.contact_view,name="contact_view"),
    path('admin_login',views.admin_login,name="admin_login"),
    path('add_course',views.add_course,name="add_course"),
    path('add_ques/<id>/<num_of_ques>/<total_mark>/',views.add_ques,name="add_ques"),
    path('admin_student', views.admin_student_view,name='admin_student'),
    path('admin_view_student', views.admin_view_student_view,name='admin_view_student'),
    path('admin_view_marks/<int:pk>', views.admin_view_marks_view,name='admin_view_marks'),
    path('admin_check_marks/<int:pk>', views.admin_check_marks_view,name='admin_check_marks'),
    path('admin_view_student_marks', views.admin_view_student_marks_view,name='admin_view_student_marks'),
    path('delete_student/<int:pk>', views.delete_student_view,name='delete_student'),
    path('delete_contact/<int:pk>', views.delete_contact_view,name='delete_contact'),
    path('logout/', views.admin_logout, name="logout"),

    

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)