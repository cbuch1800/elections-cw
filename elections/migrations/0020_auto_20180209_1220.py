# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-02-09 08:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('elections', '0019_auto_20180203_1312'),
    ]

    operations = [
        migrations.AlterField(
            model_name='election',
            name='CandidateReg',
            field=models.BooleanField(default=True),
        ),
    ]
