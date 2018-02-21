# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-02-12 09:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('elections', '0020_auto_20180209_1220'),
    ]

    operations = [
        migrations.AddField(
            model_name='election',
            name='Description',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='election',
            name='FlipGrid',
            field=models.URLField(blank=True, null=True),
        ),
    ]