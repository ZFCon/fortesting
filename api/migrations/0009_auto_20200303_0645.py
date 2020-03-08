# Generated by Django 2.2 on 2020-03-03 14:45

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_auto_20200303_0643'),
    ]

    operations = [
        migrations.AlterField(
            model_name='geg',
            name='number',
            field=models.CharField(blank=True, max_length=50, null=True, validators=[django.core.validators.RegexValidator(message='number should be like this 0100000000.', regex='^(01)[0-9]{8}')]),
        ),
    ]
