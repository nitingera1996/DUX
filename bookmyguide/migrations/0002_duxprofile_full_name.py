# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2018-02-03 11:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookmyguide', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='duxprofile',
            name='full_name',
            field=models.CharField(default='Nitin Gera', max_length=200),
            preserve_default=False,
        ),
    ]
