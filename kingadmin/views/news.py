#!/usr/bin/env python
# -*- coding=utf-8 -*-
from django.shortcuts import render, redirect
from django.views import View
from repository.models import News as Mnews


class News(View):

    def get(self, request, *args, **kwargs):
        news_list = Mnews.objects.all()
        return render(request, 'kingadmin/news.html', locals())

class Newsadd(View):

    def get(self, request, *args, **kwargs):

        return render(request, 'kingadmin/newsadd.html', locals())