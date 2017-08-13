# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-13 05:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('paranuara_api', '0005_add_employees'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='friends',
            field=models.ManyToManyField(blank=True, 
                                         related_name='friend_of', 
                                         to='paranuara_api.Person'),
        ),
    ]
