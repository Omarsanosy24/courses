# Generated by Django 4.1.1 on 2022-12-04 14:17

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('course', '0004_alter_catcourses_teacher'),
    ]

    operations = [
        migrations.AlterField(
            model_name='catcourses',
            name='users',
            field=models.ManyToManyField(blank=True, null=True, to=settings.AUTH_USER_MODEL),
        ),
    ]
