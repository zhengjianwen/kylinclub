# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2017-07-18 05:34
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('repository', '0013_auto_20170718_1319'),
    ]

    operations = [
        migrations.CreateModel(
            name='MainMenu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('caption', models.CharField(max_length=32)),
            ],
            options={
                'verbose_name_plural': '2-1后台主菜单表',
            },
        ),
        migrations.CreateModel(
            name='Role2AdminMenuAction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.AlterModelOptions(
            name='action',
            options={'verbose_name_plural': '2-1权限编码表'},
        ),
        migrations.AlterModelOptions(
            name='adminmenu',
            options={'verbose_name_plural': '2-2后台菜单链接表'},
        ),
        migrations.AlterModelOptions(
            name='adminmenuaction',
            options={'verbose_name_plural': '2-3详细权限表'},
        ),
        migrations.AddField(
            model_name='role2adminmenuaction',
            name='rama',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='repository.AdminMenuAction'),
        ),
        migrations.AddField(
            model_name='role2adminmenuaction',
            name='role',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='repository.Role'),
        ),
        migrations.AddField(
            model_name='adminmenu',
            name='mainmenu',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='repository.MainMenu'),
            preserve_default=False,
        ),
    ]
