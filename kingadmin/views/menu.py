#!/usr/bin/env python
# -*- coding=utf-8 -*-
from django.shortcuts import render, redirect
from django.views import View
from repository.models import Menu, ActivityClass, Activity
from kingadmin.kingform import MenuForm, ActivityClassForm


class MenuView(View):
    def get(self, request, *args, **kwargs):
        menu_list = Menu.objects.filter().order_by('weight')
        return render(request, 'kingadmin/menus.html', locals())


class MenuEdit(View):
    title = '菜单编辑'

    def get(self, request, cid):
        menu_obj = Menu.objects.filter(id=cid).first()
        in_form = {
            'weight': menu_obj.weight,
            'status': menu_obj.status,
            'name': menu_obj.name,
            'url': menu_obj.url,
        }
        obj = MenuForm(initial=in_form)
        return render(request, 'kingadmin/menuadd.html', locals())

    def post(self, request, cid):
        obj = MenuForm(request.POST)
        if obj.is_valid():
            menu_obj = Menu.objects.filter(id=cid).update(**obj.cleaned_data)
            return redirect('/kingadmin/menus')
        return render(request, 'kingadmin/menuadd.html', locals())


class Activitytype(View):
    def get(self, request):
        huodong_list = ActivityClass.objects.all()
        return render(request, 'kingadmin/activitytype.html', locals())


class Activitytypeadd(View):
    title = '活动新增'
    def get(self, request):
        obj = ActivityClassForm()
        return render(request, 'kingadmin/activitypeedit.html', locals())

    def post(self, request):
        obj = ActivityClassForm(request.POST)
        if obj.is_valid():
            ActivityClass.objects.create(**obj.cleaned_data)
            return redirect('kingadmin/activitytype/')
        return render(request, 'kingadmin/activitypeedit.html', locals())


class Activitytypeedit(View):
    title = '活动类型编辑'
    def get(self, request, cid):
        a_obj = ActivityClass.objects.filter(id=cid).first()
        in_form = {
            'menu': a_obj.menu,
            'alias': a_obj.alias,
            'name': a_obj.name,
            'content': a_obj.content
        }
        obj = ActivityClassForm(initial=in_form)
        return render(request, 'kingadmin/activitypeedit.html', locals())

    def post(self, request, cid):
        obj = ActivityClassForm(request.POST)
        if obj.is_valid():
            ActivityClass.objects.filter(id=cid).update(**obj.cleaned_data)
            return redirect('kingadmin/activitytype/')
        return render(request, 'kingadmin/activitypeedit.html', locals())


class Activityadd(View):
    def get(self, request):
        activity_list = ActivityClass.objects.all()
        return render(request, 'kingadmin/activitypeedit.html', locals())


class ActivityView(View):
    def get(self, request):
        activity_list = Activity.objects.all()
        return render(request, 'kingadmin/activitylist.html', locals())
