# Generated by Django 4.1.1 on 2022-12-05 14:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0011_cart_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='url',
            field=models.TextField(blank=True, null=True),
        ),
    ]