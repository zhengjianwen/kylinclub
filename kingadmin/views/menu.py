#!/usr/bin/env python
# -*- coding=utf-8 -*-
from django.shortcuts import render, redirect
from .baseview import BaseView
from repository.models import Menu, ActivityClass, Activity
from kingadmin.kingform import MenuForm, ActivityClassForm,ActivityForm


class MenuView(BaseView):
    def get(self, request, *args, **kwargs):
        menu_list = Menu.objects.filter().order_by('weight')
        return render(request, 'kingadmin/menus/menus.html', locals())


class MenuAdd(BaseView):
    title = '菜单添加'

    def get(self, request):
        obj = MenuForm()
        return render(request, 'kingadmin/menus/menuadd.html', locals())

    def post(self, request):
        obj = MenuForm(request.POST)
        if obj.is_valid():
            Menu.objects.create(**obj.cleaned_data)
            return redirect('/kingadmin/menus')
        return render(request, 'kingadmin/menus/menuadd.html', locals())


class MenuEdit(BaseView):
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
        return render(request, 'kingadmin/menus/menuadd.html', locals())

    def post(self, request, cid):
        obj = MenuForm(request.POST)
        if obj.is_valid():
            menu_obj = Menu.objects.filter(id=cid).update(**obj.cleaned_data)
            return redirect('/kingadmin/menus')
        return render(request, 'kingadmin/menus/menuadd.html', locals())


class Activitytype(BaseView):
    def get(self, request):
        huodong_list = ActivityClass.objects.all()
        return render(request, 'kingadmin/atype/activitytype.html', locals())


class Activitytypeadd(BaseView):
    title = '活动新增'
    def get(self, request):
        obj = ActivityClassForm()
        return render(request, 'kingadmin/atype/activitypeedit.html', locals())

    def post(self, request):
        obj = ActivityClassForm(request.POST)
        if obj.is_valid():
            ActivityClass.objects.create(**obj.cleaned_data)
            return redirect('/kingadmin/activitytype/')
        return render(request, 'kingadmin/atype/activitypeedit.html', locals())


class Activitytypeedit(BaseView):
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
        return render(request, 'kingadmin/atype/activitypeedit.html', locals())

    def post(self, request, cid):
        obj = ActivityClassForm(request.POST)
        if obj.is_valid():
            ActivityClass.objects.filter(id=cid).update(**obj.cleaned_data)
            return redirect('kingadmin/activitytype/')
        return render(request, 'kingadmin/atype/activitypeedit.html', locals())


class Activityadd(BaseView):
    title = '添加活动'
    def get(self, request):
        obj = ActivityForm()
        return render(request, 'kingadmin/activity/activtyedit.html', locals())

    def post(self,request):
        obj = ActivityForm(request.POST, request.FILES)
        if obj.is_valid():
            cid = obj.cleaned_data.get('activityclass')
            obj.cleaned_data['activityclass'] = ActivityClass.objects.filter(id=cid).first()
            Activity.objects.create(**obj.cleaned_data)
            if obj.cleaned_data.get('img'):
                self.save_img(obj.cleaned_data['img'], 'activity')
            return redirect('/kingadmin/activity.html')
        print('===>添加活动错误', obj.errors)
        return render(request, 'kingadmin/activtyedit.html', locals())


class Activityedit(BaseView):
    title = '活动编辑'

    def get(self, request, cid):
        data = Activity.objects.filter(id=cid).first()
        in_form = {
            'activityclass':data.activityclass,
            'img':data.img,
            'title':data.title,
            'summary':data.summary,
            'content':data.content,
            'author':data.author,
            'up':data.up,
            'status':data.status,
            'create_at':data.create_at,
        }
        obj = ActivityForm(initial=in_form)
        return render(request, '/kingadmin/activtyedit.html', locals())

    def post(self, request, cid):
        obj = ActivityForm(request.POST, request.FILES)
        if obj.is_valid():
            cobj = Activity.objects.filter(id=cid).update(**obj.cleaned_data)
            if obj.cleaned_data.get('img'):
                self.save_img(obj.cleaned_data['img'], 'activity')
            return redirect('/kingadmin/activitylist.html')
        print('===>编辑活动错误',obj.errors)
        return render(request, '/kingadmin/activtyedit.html', locals())


class ActivityView(BaseView):
    def get(self, request):
        activity_list = Activity.objects.all()
        return render(request, 'kingadmin/activity/activitylist.html', locals())
