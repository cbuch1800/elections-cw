# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-01-10 17:35
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('elections', '0015_completeballot_vote'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='CastBallot',
            new_name='BallotCast',
        ),
    ]
