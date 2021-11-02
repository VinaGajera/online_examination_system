from django.db import models
from Student.models import Signup

# Create your models here.
class Course(models.Model):
    course_name = models.CharField(max_length=50)
    number_of_question = models.IntegerField()
    total_marks = models.IntegerField()
    passing_marks=models.IntegerField()
    
class Question(models.Model):
    course=models.ForeignKey(Course,on_delete=models.CASCADE)
    marks=models.PositiveIntegerField()
    question=models.CharField(max_length=600)
    option1=models.CharField(max_length=200)
    option2=models.CharField(max_length=200)
    option3=models.CharField(max_length=200)
    cat=(('Option1','Option1'),('Option2','Option2'),('Option3','Option3'))
    answer=models.CharField(max_length=200,choices=cat)

class Contact(models.Model):
    name=models.CharField(max_length=50)
    email_id=models.CharField(max_length=50)
    contact_no=models.CharField(max_length=12)
    message=models.TextField()
    
    def __str__(self):
            return self.name +"\t <"+ self.email_id + ">"

class Result(models.Model):
    student = models.ForeignKey(Signup,on_delete=models.CASCADE)
    exam = models.ForeignKey(Course,on_delete=models.CASCADE)
    marks = models.PositiveIntegerField()
    date = models.DateTimeField(auto_now=True)