# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2017-07-08 09:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('repository', '0004_emailtemplate_effect'),
    ]

    operations = [
        migrations.AddField(
            model_name='emailtemplate',
            name='status',
            field=models.BooleanField(default=0, verbose_name='状态'),
        ),
    ]
