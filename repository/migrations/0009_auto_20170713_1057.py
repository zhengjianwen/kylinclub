# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2017-07-13 02:57
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('repository', '0008_auto_20170711_1747'),
    ]

    operations = [
        migrations.AlterField(
            model_name='role2user',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='repository.UserInfo'),
        ),
    ]