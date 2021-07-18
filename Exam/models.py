from django.db import models
from django.db.models.fields import CharField
from datetime import datetime
from django.utils.timezone import now



# Create your models here.
class Contact(models.Model):
    name=models.CharField(max_length=50)
    email_id=models.CharField(max_length=50)
    contact_no=models.CharField(max_length=12)
    message=models.TextField()
    datetime=models.DateField(blank=True,default=datetime(1111,11,11),null=True)

    def __str__(self):
            return self.name +"\t <"+ self.email_id + ">"

class Course(models.Model):
    course_name = models.CharField(max_length=50)
    question_number = models.PositiveIntegerField()
    total_marks = models.PositiveIntegerField()
    #passing_marks=models.PositiveIntegerField()
    datetime=models.DateField(blank=True,default=datetime(1111,11,11),null=True)

    def __str__(self):
            return self.course_name

class Question(models.Model):
    course=models.ForeignKey(Course,on_delete=models.CASCADE)
    # i=0;
    # {% for i in question_number %}
    #     {% if i < question_number%}
    #         <input type="next" name="next" class="btn btn-primary" value="Next" disabled/>
        #             
            
    #     {% else %}
    #       <input type="submit" name="_save" class="btn btn-primary" value="Save" disabled/>
            
    #     {% endif %}
    # {% endfor %}
    marks=models.PositiveIntegerField()
    question=models.CharField(max_length=600)
    option1=models.CharField(max_length=200)
    option2=models.CharField(max_length=200)
    option3=models.CharField(max_length=200)
    option4=models.CharField(max_length=200)
    cat=(('Option1','Option1'),('Option2','Option2'),('Option3','Option3'),('Option4','Option4'))
    answer=models.CharField(max_length=200,choices=cat)