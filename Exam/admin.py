from django.contrib import admin
from .models import Contact, Course, Question

class CourseAdmin(admin.ModelAdmin):
    list_display=('course_name','datetime',)
    
    
admin.site.register(Contact)
admin.site.register(Course,CourseAdmin)
admin.site.register(Question)