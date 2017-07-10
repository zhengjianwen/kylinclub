#!/usr/bin/env python
# -*- coding=utf-8 -*-
from django.shortcuts import render, redirect, HttpResponse
from repository.models import Email, EmailTemplate, Emaillog
from kingadmin.kingform import MailForm, EmailTmplatForm
from .baseview import BaseView
from utils.pages import Pagination
import json


class EmailView(BaseView):
    def get(self, request):
        mail_list = Email.objects.all()
        return render(request, 'kingadmin/mail/maillist.html', locals())


class EmailAdd(BaseView):
    title = '添加邮件'

    def get(self, request, *args, **kwargs):
        obj = MailForm()
        return render(request, 'kingadmin/mail/editemail.html', locals())

    def post(self, request, *args, **kwargs):
        obj = MailForm(request.POST)
        if obj.is_valid():
            Email.objects.create(**obj.cleaned_data)
            return redirect('/kingadmin/mailset/')
        return render(request, 'kingadmin/mail/editemail.html', locals())


class EmailEdit(BaseView):
    title = '编辑邮件'

    def get(self, request, cid, *args, **kwargs):
        email = Email.objects.filter(id=cid).first()
        in_form = {
            'mail_type': email.mail_type,
            'addr': email.addr,
            'user': email.user,
            'password': email.password,
            'port': email.port,
            'is_ssh': email.is_ssh,
        }
        obj = MailForm(initial=in_form)
        return render(request, 'kingadmin/mail/editemail.html', locals())

    def post(self, request, cid, *args, **kwargs):
        obj = MailForm(request.POST)
        if obj.is_valid():
            Email.objects.filter(id=cid).update(**obj.cleaned_data)
            return redirect('/kingadmin/mailset/')
        return render(request, 'kingadmin/mail/editemail.html', locals())


def maildelete(request, cid):
    Email.objects.filter(id=cid).delete()
    return redirect('/kingadmin/mainset/')


class EmailTmplatView(BaseView):
    title = '模板列表'

    def get(self, request):
        obj_list = EmailTemplate.objects.all()
        return render(request, 'kingadmin/moban/email.html', locals())


class EmailTmplatAdd(BaseView):
    title = '模板列表'

    def get(self, request):
        obj = EmailTmplatForm()
        return render(request, 'kingadmin/moban/mailedit.html', locals())

    def post(self, request):
        obj = EmailTmplatForm(request.POST)
        if obj.is_valid():
            EmailTemplate.objects.create(**obj.cleaned_data)
            return redirect('/kingadmin/mailmb/')
        return render(request, 'kingadmin/moban/mailedit.html', locals())


class EmailTmplatEdit(BaseView):
    title = '模板列表'

    def get(self, request, cid):
        mail_obj = EmailTemplate.objects.filter(id=cid).first()
        in_form = {
            'effect': mail_obj.effect,
            'status': mail_obj.status,
            'name': mail_obj.name,
            'content': mail_obj.content,
            'sendmail_id': mail_obj.sendmail,
        }
        obj = EmailTmplatForm(initial=in_form)
        return render(request, 'kingadmin/moban/mailedit.html', locals())

    def post(self, request, cid):
        obj = EmailTmplatForm(request.POST)
        if obj.is_valid():
            EmailTemplate.objects.filter(id=cid).update(**obj.cleaned_data)
            return redirect('/kingadmin/mailmb/')
        return render(request, 'kingadmin/moban/mailedit.html', locals())


def emailtmplatstatus(request, cid):
    status = request.GET.get('status', 0)
    EmailTemplate.objects.filter(id=cid).update(status=status)
    return redirect('/kingadmin/mailmb/')


def maillog(request):
    data = Emaillog.objects.all()
    now_page = request.GET.get('p', 1)
    haed_url = ''
    page_obj = Pagination(data.count(), now_page, haed_url, 10, 5)
    data_list = data[page_obj.start:page_obj.end]
    return render(request, 'kingadmin/mail/emaillog.html', locals())
