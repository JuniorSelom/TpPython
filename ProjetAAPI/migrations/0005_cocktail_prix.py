# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-01 17:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ProjetAAPI', '0004_auto_20170609_1817'),
    ]

    operations = [
        migrations.AddField(
            model_name='cocktail',
            name='prix',
            field=models.IntegerField(default=5),
        ),
    ]
