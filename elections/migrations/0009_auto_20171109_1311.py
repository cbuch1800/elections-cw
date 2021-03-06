# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-09 09:11
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('elections', '0008_castballot_completeballot'),
    ]

    operations = [
        migrations.CreateModel(
            name='AllowToRegister',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ElectionID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='elections.Election')),
                ('UserTypeID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='elections.UserType')),
            ],
        ),
        migrations.AlterField(
            model_name='post',
            name='Timestamp',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
