#!/usr/bin/env python
# -*- coding=utf-8 -*-
from django.shortcuts import render, redirect,HttpResponse
from repository.models import Email,EmailTemplate,Emaillog
from kingadmin.kingform import MailForm,EmailTmplatForm
from .baseview import BaseView
from utils.pages import Pagination
import json


class EmailView(BaseView):
    def get(self, request, *args, **kwargs):
        email = Email.objects.all().first()
        if email:
            in_form = {
                'mail_type':email.mail_type,
                'addr':email.addr,
                'user':email.user,
                'password':email.password,
                'port':email.port,
                'is_ssh':email.is_ssh,
            }
            print(in_form)
            obj = MailForm(initial=in_form)
        else:
            obj = MailForm()
        return render(request, 'kingadmin/mail/email.html', locals())

    def post(self,request):
        data = {'status':0,'msg':'','data':''}
        email = Email.objects.all().first()
        obj = MailForm(request.POST)
        if obj.is_valid():
            if not email:
                ret = Email.objects.create(**obj.cleaned_data)
                if ret:
                    data['msg'] = '创建成功'
                else:
                    data['status'] = 1
                    data['msg'] = '创建失败'
            else:
                ret = Email.objects.all().update(**obj.cleaned_data)
                if ret:
                    data['msg'] = '更新成功'
                else:
                    data['status'] = 1
                    data['msg'] = '更新失败'
        else:
            data['status'] = 1
            data['msg'] = '验证失败'
            data['data'] = '%s' % obj.errors
        return HttpResponse(json.dumps(data))


class EmailTmplatView(BaseView):
    title = '模板列表'

    def get(self,request):
        obj_list = EmailTemplate.objects.all()
        return render(request,'kingadmin/moban/email.html',locals())


class EmailTmplatAdd(BaseView):
    title = '模板列表'

    def get(self, request):
        obj = EmailTmplatForm()
        return render(request, 'kingadmin/moban/mailedit.html', locals())

    def post(self,request):
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
            'effect':mail_obj.effect,
            'status':mail_obj.status,
            'name':mail_obj.name,
            'content':mail_obj.content,
        }
        obj = EmailTmplatForm(initial=in_form)
        return render(request, 'kingadmin/moban/mailedit.html', locals())

    def post(self, request, cid):
        obj = EmailTmplatForm(request.POST)
        if obj.is_valid():
            EmailTemplate.objects.filter(id=cid).update(**obj.cleaned_data)
            return redirect('/kingadmin/mailmb/')
        return render(request, 'kingadmin/moban/mailedit.html', locals())


def emailtmplatstatus(request,cid):
    status=request.GET.get('status', 0)
    EmailTemplate.objects.filter(id=cid).update(status=status)
    return redirect('/kingadmin/mailmb/')

def maillog(request):
    data = Emaillog.objects.all()
    now_page = request.GET.get('p',1)
    haed_url = ''
    page_obj = Pagination(data.count(), now_page, haed_url, 10, 5)
    data_list = data[page_obj.start:page_obj.end]
    return render(request,'kingadmin/mail/emaillog.html',locals())