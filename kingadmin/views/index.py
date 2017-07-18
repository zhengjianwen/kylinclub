#!/usr/bin/env python
# -*- coding=utf-8 -*-
from django.shortcuts import render, redirect
from django.views import View
from repository.models import *

class Index(View):

    def get(self,request):
        usernub = UserInfo.objects.filter(status=1).count()
        alluser = UserInfo.objects.count()
        zhanbi = usernub/alluser*100
        qiye = CompanyMember.objects.filter(status=4).count()
        qyzb =qiye/CompanyMember.objects.count()*100
        huodong = Activity.objects.count()

        return render(request, 'kingadmin/index.html', locals())