#!/usr/bin/env python
# -*- coding=utf-8 -*-
from django.shortcuts import render, redirect
from django.views import View


class Index(View):

    def get(self,request):

        return render(request, 'kingadmin/index.html', locals())