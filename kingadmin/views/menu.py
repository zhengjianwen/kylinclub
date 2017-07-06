#!/usr/bin/env python
# -*- coding=utf-8 -*-
from django.shortcuts import render, redirect
from django.views import View
from repository.models import Menu,ActivityClass,Activity


class MenuView(View):

    def get(self, request, *args, **kwargs):
        menu_list = Menu.objects.all()
        return render(request, 'kingadmin/menus.html', locals())


class Activitytype(View):

    def get(self,request):
        huodong_list = ActivityClass.objects.all()
        return render(request,'kingadmin/activitytype.html',locals())


class Activityadd(View):

    def get(self,request):
        activity_list = ActivityClass.objects.all()
        return render(request, 'kingadmin/activityadd.html',locals())


class ActivityView(View):

    def get(self,request):
        activity_list = Activity.objects.all()
        return render(request, 'kingadmin/activity.html',locals())

