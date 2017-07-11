#!/usr/bin/env python
# -*- coding=utf-8 -*-
from django.shortcuts import render, redirect
from repository.models import News
from kingadmin.kingform import NewForm
from .baseview import BaseView
from utils.pages import Pagination


class NewsView(BaseView):
    def get(self, request, *args, **kwargs):
        now_page = request.GET.get('p',1)
        haed_url = ''
        news_list = News.objects.all()
        page_obj = Pagination(news_list.count(), now_page, haed_url,10,5)

        news_list = news_list[page_obj.start:page_obj.end]
        return render(request, 'kingadmin/news/news.html', locals())


class Newsadd(BaseView):
    def get(self, request, *args, **kwargs):
        obj = NewForm()
        return render(request, 'kingadmin/news/newsadd.html', locals())

    def post(self, request, *args, **kwargs):
        obj = NewForm(request.POST, request.FILES)
        if obj.is_valid():
            if obj.cleaned_data.get('img'):
                path = self.save_img(obj.cleaned_data.get('img'), 'news')
                obj.cleaned_data['img'] = path
            new_obj = News.objects.create(**obj.cleaned_data)
            return redirect('/kingadmin/news/')
        return render(request, 'kingadmin/news/newsadd.html', locals())


class NewsEdit(BaseView):
    def get(self, request, cid, *args, **kwargs):
        new_obj = News.objects.filter(id=cid).first()
        in_form = {
            'title': new_obj.title,
            'summary': new_obj.summary,
            'content': new_obj.content,
            'img': new_obj.img,
            'author': new_obj.author,
            'up': new_obj.up,
            'creat_at': new_obj.creat_at,
            'status': new_obj.status
        }
        obj = NewForm(initial=in_form)
        return render(request, 'kingadmin/news/newsadd.html', locals())

    def post(self, request, cid, *args, **kwargs):
        obj = NewForm(request.POST, request.FILES)
        if obj.is_valid():
            if not obj.cleaned_data.get('img'):
                del obj.cleaned_data['img']
            else:
                path = self.save_img(obj.cleaned_data['img'], 'news')
                obj.cleaned_data['img'] = path
            new_obj = News.objects.filter(id=cid).update(**obj.cleaned_data)
            return redirect('/kingadmin/news/')
        return render(request, 'kingadmin/news/newsadd.html', locals())


def delete_new(request,cid):
    News.objects.filter(id=cid).delete()
    return redirect('/kingadmin/news/')


def status_new(request,cid):
    status = request.GET.get('status', 0)
    News.objects.filter(id=cid).update(status=status)
    return redirect('/kingadmin/news/')