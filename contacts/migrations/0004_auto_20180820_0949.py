# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-08-20 13:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0003_auto_20180820_0949'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='dob',
            field=models.DateField(null=True),
        ),
    ]