# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-26 16:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('elections', '0004_profile'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('UserType', models.CharField(max_length=10)),
            ],
        ),
    ]