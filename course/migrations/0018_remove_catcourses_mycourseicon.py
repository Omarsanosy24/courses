# Generated by Django 4.1.1 on 2022-12-11 14:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0017_catcourses_mycourseicon'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='catcourses',
            name='myCourseIcon',
        ),
    ]