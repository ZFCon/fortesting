# Generated by Django 2.2 on 2020-03-03 14:41

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_auto_20200301_0423'),
    ]

    operations = [
        migrations.AlterField(
            model_name='geg',
            name='number',
            field=models.CharField(blank=True, max_length=50, null=True, validators=[django.core.validators.RegexValidator(message='Hashtag doesnt comply', regex='(201)[0-9]{9}')]),
        ),
    ]
