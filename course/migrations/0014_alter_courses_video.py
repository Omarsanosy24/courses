# Generated by Django 4.1.1 on 2022-12-09 20:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0013_alter_courses_catcourses'),
    ]

    operations = [
        migrations.AlterField(
            model_name='courses',
            name='video',
            field=models.TextField(),
        ),
    ]
