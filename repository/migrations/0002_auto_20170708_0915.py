# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2017-07-08 01:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('repository', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activity',
            name='img',
            field=models.ImageField(null=True, upload_to='activity', verbose_name='图片'),
        ),
    ]
