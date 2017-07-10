#!/usr/bin/env python
# -*- coding=utf-8 -*-
from django.shortcuts import render, redirect, HttpResponse
from repository.models import Carousel, Rotation
from kingadmin.kingform import MailForm, EmailTmplatForm
from .baseview import BaseView
from utils.pages import Pagination


class EmailView(BaseView):
    def get(self, request):
        carousel_list = Carousel.objects.all()
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