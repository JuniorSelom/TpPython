# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-03 12:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ProjetAAPI', '0005_cocktail_prix'),
    ]

    operations = [
        migrations.AlterField(
            model_name='queue',
            name='date',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='queue',
            name='state',
            field=models.CharField(default=1, max_length=20),
        ),
    ]
