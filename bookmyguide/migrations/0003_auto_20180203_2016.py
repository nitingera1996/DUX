# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2018-02-03 20:16
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookmyguide', '0002_duxprofile_full_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='places',
            name='description',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='places',
            name='likes',
            field=models.BigIntegerField(default=100),
        ),
        migrations.AddField(
            model_name='places',
            name='photo',
            field=models.TextField(blank=True, validators=[django.core.validators.URLValidator()]),
        ),
        migrations.AlterField(
            model_name='places',
            name='name',
            field=models.CharField(max_length=200, unique=True),
        ),
    ]