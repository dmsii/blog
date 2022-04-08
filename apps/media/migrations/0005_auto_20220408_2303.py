# Generated by Django 2.2.5 on 2022-04-08 23:03

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('media', '0004_media_creator'),
    ]

    operations = [
        migrations.AlterField(
            model_name='media',
            name='filepath',
            field=models.CharField(max_length=400, validators=[django.core.validators.MinLengthValidator(1)]),
        ),
    ]
