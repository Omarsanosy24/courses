# Generated by Django 4.1.1 on 2022-12-03 13:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0002_cart_catcourses_users_alter_catcourses_year_cartitem'),
    ]

    operations = [
        migrations.AddField(
            model_name='catcourses',
            name='teacher',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='course.teacher'),
        ),
    ]