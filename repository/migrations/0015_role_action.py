# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2017-07-18 05:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('repository', '0014_auto_20170718_1334'),
    ]

    operations = [
        migrations.AddField(
            model_name='role',
            name='action',
            field=models.ManyToManyField(through='repository.Role2AdminMenuAction', to='repository.AdminMenuAction'),
        ),
    ]