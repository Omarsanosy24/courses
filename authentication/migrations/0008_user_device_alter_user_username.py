# Generated by Django 4.1.1 on 2022-12-01 21:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0007_alter_user_username'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='device',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(max_length=255),
        ),
    ]
