# Generated by Django 4.1.3 on 2022-12-11 11:12

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0002_category_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=models.CharField(max_length=10, unique=True, validators=[django.core.validators.MinLengthValidator(0)]),
        ),
    ]
