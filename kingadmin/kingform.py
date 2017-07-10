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
        attrs={'class': "form-control", 'type': 'date'}
    ))
    status = fields.ChoiceField(choices=((0, '显示'), (1, '隐藏')))

    def clean_author(self):
        val = self.cleaned_data['author']
        if val == '':
            val = 'admin'
        return val

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
    menu_id = fields.CharField(widget=widgets.Select(
        attrs={'class': "form-control col-md-7 col-xs-12"}
    ))
    alias = fields.CharField(max_length=32, min_length=1, strip=True, required=True,
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
        super(ActivityClassForm, self).__init__(*args, **kwargs)
        self.fields['menu_id'].widget.choices = Menu.objects.all().values_list('id', 'name')


class ActivityForm(Form):
    activityclass_id = fields.CharField(widget=widgets.Select(
        attrs={'class': "form-control col-md-7 col-xs-12"}
    ))
    img = fields.ImageField(required=False,
                            widget=widgets.FileInput(attrs={'class': "form-control col-md-7 col-xs-12"}))
    title = fields.CharField(max_length=128,
                             min_length=1,
                             widget=widgets.TextInput(
                                 attrs={'placeholder': "请填写活动标题", 'class': "form-control col-md-7 col-xs-12"}
                             ))
    summary = fields.CharField(max_length=255,
                               widget=widgets.TextInput(
                                   attrs={'placeholder': "简介，作为首页展示用",
                                          'class': "form-control col-md-7 col-xs-12"}
                               ))
    content = fields.CharField(widget=widgets.Textarea(
        attrs={'class': 'form-control',
               'placeholder': '请在此填写活动内容',
               'rows': '10',
               'id': 'mycontent'}))
    author = fields.CharField(required=False, max_length=64,
                              widget=widgets.TextInput(
                                  attrs={'placeholder': "默认为admin", 'class': "form-control col-md-7 col-xs-12"}
                              ))
    up = fields.IntegerField(required=False,
                             widget=widgets.TextInput(
                                 attrs={'placeholder': "可以自定义数字",
                                        'class': "form-control col-md-7 col-xs-12"}))
    status = fields.ChoiceField(choices=((0, '显示'), (1, '隐藏')))
    create_at = fields.DateField(widget=widgets.DateTimeInput(
        attrs={'class': "form-control col-md-7 col-xs-12", 'type': 'date'}))

    def __init__(self, *args, **kwargs):
        super(ActivityForm, self).__init__(*args, **kwargs)
        self.fields['activityclass_id'].widget.choices = ActivityClass.objects.all().values_list('id', 'name')

    def clean_up(self):
        val = self.cleaned_data['up']
        if not val:
            val = 1
        return val

    class Meta:
        model = Activity


class MailForm(Form):
    mail_type = fields.ChoiceField(choices=((0, 'SMTP'), (1, 'IMAP')),
                                   widget=widgets.Select(
                                       attrs={'class': 'form-control'}
                                   ))
    user = fields.EmailField(max_length=128,
                             min_length=6,
                             widget=widgets.TextInput(
                                 attrs={'placeholder': "请填写发送邮件地址:如 abc@163.com",
                                        'class': "form-control col-md-7 col-xs-12"}
                             ))
    password = fields.CharField(max_length=128,
                                min_length=1,
                                widget=widgets.PasswordInput(
                                    attrs={'placeholder': "请输入邮箱密码,提交新必须写密码。",
                                           'class': "form-control col-md-7 col-xs-12"}
                                ))
    addr = fields.CharField(max_length=128,
                            min_length=1,
                            widget=widgets.TextInput(
                                attrs={'placeholder': "请输入提交的smtp或imap地址。",
                                       'class': "form-control col-md-7 col-xs-12"}
                            ))
    port = fields.IntegerField(max_value=65535, min_value=1, required=False,
                               widget=widgets.TextInput(
                                   attrs={'placeholder': "请填写端口，无加密端口为：25，加密端口为：465",
                                          'class': "form-control col-md-7 col-xs-12"}
                               ))
    is_ssh = fields.BooleanField(required=False)

    def clean_is_shh(self):
        val = self.cleaned_data['is_ssh']
        if not val:
            val = 1
        return val

    def clean_port(self):
        val = self.cleaned_data['port']
        if not val:
            val = 25
        return val


class EmailTmplatForm(Form):
    effect = fields.ChoiceField(choices=EmailTemplate.effect_choices)
    status = fields.ChoiceField(choices=((0, '显示'), (1, '隐藏')))
    sendmail_id = fields.CharField(widget=widgets.Select(
        attrs={'class': "form-control col-md-7 col-xs-12"}))
    name = fields.CharField(max_length=128, min_length=1,
                            widget=widgets.TextInput(
                                attrs={'placeholder': "请填写模板名称", 'class': "form-control col-md-7 col-xs-12"}
                            ))

    content = fields.CharField(widget=widgets.Textarea(
        attrs={'class': 'form-control',
               'rows': '10',
               'id': 'mycontent'}))

    def __init__(self, *args, **kwargs):
        super(EmailTmplatForm, self).__init__(*args, **kwargs)
        self.fields['sendmail_id'].widget.choices = Email.objects.all().values_list('id', 'user')


class CarouselForm(Form):
    weight = fields.IntegerField(widget=widgets.TextInput(
                                     attrs={'placeholder': "显示排名，数字越大排名越前", 'class': "form-control col-md-7 col-xs-12"}
                                 ))
    status = fields.ChoiceField(choices=((0, '显示'), (1, '隐藏')))
    orgid_id = fields.CharField(widget=widgets.Select(
        attrs={'class': "form-control col-md-7 col-xs-12"}))
    title = fields.CharField(max_length=64, min_length=1, required=True,
                             widget=widgets.TextInput(
                                 attrs={'placeholder': "标题", 'class': "form-control col-md-7 col-xs-12"}
                             ))
    content = fields.CharField(widget=widgets.Textarea(
        attrs={'class': 'form-control',
               'rows': '10',
               'id': 'mycontent'}))
    url = fields.CharField(max_length=128, min_length=0, required=False,
                           widget=widgets.TextInput(
                               attrs={'placeholder': "填写链接地址",
                                      'class': "form-control col-md-7 col-xs-12"}
                           ))
    img = fields.ImageField(required=True,
                            widget=widgets.FileInput(attrs={'class': "form-control col-md-7 col-xs-12"}))

    def __init__(self, *args, **kwargs):
        super(CarouselForm, self).__init__(*args, **kwargs)
        self.fields['orgid_id'].widget.choices = Rotation.objects.all().values_list('id', 'name')
