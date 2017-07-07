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
        attrs={'class': "form-control col-md-7 col-xs-12", 'type': 'date'}
    ))
    status = fields.ChoiceField(choices=((0, '显示'), (1, '隐藏')))

    class Meta:
        model = News


class MenuForm(Form):
    weight = fields.IntegerField(max_value=999,
                                 min_value=1,
                                 widget=widgets.NumberInput(
                                     attrs={'placeholder': "数字越大排名越前", 'class': "form-control col-md-7 col-xs-12"}
                                 ))
    status = fields.ChoiceField(choices=((0, '显示'), (1, '隐藏')))
    name = fields.CharField(max_length=64, min_length=1, strip=True,
                            widget=widgets.TextInput(
                                attrs={'placeholder': "菜单名称", 'class': "form-control col-md-7 col-xs-12"}
                            ))
    url = fields.CharField(required=False, strip=True,
                          widget=widgets.TextInput(
                              attrs={'placeholder': "链接地址", 'class': "form-control col-md-7 col-xs-12"}
                          ))

    def clean_name(self):
        data = self.cleaned_data['name']
        # if Menu.objects.filter(name=data).count():
        #     raise ValidationError('菜单已存在，请重新输入。', 'invalid')
        return data

    class Meta:
        model = Menu


class ActivityClassForm(Form):
    menu = fields.CharField(widget=widgets.Select(
        attrs={'class': "form-control col-md-7 col-xs-12"}
    ))
    alias = fields.CharField(max_length=32, min_length=1, strip=True,required=True,
                             widget=widgets.TextInput(
                                attrs={'placeholder': "菜单别名，必须为英文", 'class': "form-control col-md-7 col-xs-12"}
                            ))
    name = fields.CharField(max_length=64, min_length=1, strip=True,
                            widget=widgets.TextInput(
                                attrs={'placeholder': "菜单名称", 'class': "form-control col-md-7 col-xs-12"}
                            ))
    content = fields.CharField(widget=widgets.Textarea(
                                attrs={'class': 'form-control',
                                       'placeholder': '请在此填写类型内容，在单页显示。',
                                       'rows': '10',
                                       'id': 'mycontent'}))

    def __init__(self, *args, **kwargs):
        super(ActivityClassForm, self).__init__(*args,**kwargs)
        self.fields['menu'].widget.choices = Menu.objects.all().values_list('id', 'name')

    class Meta:
        model = ActivityClass
