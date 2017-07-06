#!/usr/bin/env python
# -*- coding=utf-8 -*-
from repository.models import *
from django.forms.forms import Form
from django.forms import fields, widgets
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator


class NewForm(Form):
    title = fields.CharField(max_length=128,
                             min_length=1,
                             widget=widgets.TextInput(
                                 attrs={'placeholder': "请填写新闻标题", 'class': "form-control col-md-7 col-xs-12"}
                             ))
    img = fields.ImageField(required=False,
                            widget=widgets.FileInput(attrs={'class': "form-control col-md-7 col-xs-12"}))
    content = fields.CharField(widget=widgets.Textarea(
        attrs={'class': 'form-control',
               'placeholder': '请在此填写文章内容',
               'rows': '10',
               'id': 'mycontent'}))
    summary = fields.CharField(max_length=255,
                               widget=widgets.TextInput(
                                   attrs={'placeholder': "简介，作为首页展示用", 'class': "form-control col-md-7 col-xs-12"}
                               ))
    author = fields.CharField(required=False, max_length=64,
                              widget=widgets.TextInput(
                                  attrs={'placeholder': "默认为admin", 'class': "form-control col-md-7 col-xs-12"}
                              ))
    up = fields.IntegerField(required=False, widget=widgets.TextInput(
        attrs={'placeholder': "可以自定义数字", 'class': "form-control col-md-7 col-xs-12"}
    ))
    creat_at = fields.DateField(widget=widgets.DateTimeInput(
        attrs={'class': "form-control col-md-7 col-xs-12",'type':'date'}
    ))
    status = fields.ChoiceField(choices=((0, '显示'), (1, '隐藏')))

    class Meta:
        model = News
