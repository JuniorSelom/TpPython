# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-09 18:16
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ProjetAAPI', '0002_token'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cocktail',
            name='drink',
        ),
        migrations.AddField(
            model_name='cocktail',
            name='drinks',
            field=models.ManyToManyField(related_name='cocktails', to='ProjetAAPI.Drink'),
        ),
        migrations.AlterField(
            model_name='queue',
            name='cocktail',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ProjetAAPI.Cocktail', unique=True),
        ),
    ]
