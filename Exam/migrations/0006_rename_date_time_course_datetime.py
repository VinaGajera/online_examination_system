# Generated by Django 3.2.4 on 2021-07-17 15:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Exam', '0005_alter_course_date_time'),
    ]

    operations = [
        migrations.RenameField(
            model_name='course',
            old_name='Date_time',
            new_name='datetime',
        ),
    ]