# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-12-04 02:44
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('eBedTrack', '0002_auto_20171203_2038'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='nurse',
            name='admin_id',
        ),
    ]
