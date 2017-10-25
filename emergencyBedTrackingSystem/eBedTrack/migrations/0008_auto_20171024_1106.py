# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-10-24 16:06
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('eBedTrack', '0007_auto_20171023_1039'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bed',
            old_name='hospital_id',
            new_name='bh',
        ),
        migrations.AddField(
            model_name='hospital',
            name='created_date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]