#!/usr/bin/env python
# -*- coding=utf-8 -*-
from django.shortcuts import render, redirect,HttpResponse
from django.views import View
from repository.models import News
from kingadmin.kingform import NewForm
from kylinclub.settings import BASE_DIR
from utils.pages import Pagination
import os,json


class NewsView(View):
    def get(self, request, *args, **kwargs):
        now_page = request.GET.get('p',1)
        haed_url = ''
        news_list = News.objects.all()
        page_obj = Pagination(news_list.count(), now_page, haed_url,10,5)

        news_list = news_list[page_obj.start:page_obj.end]
        return render(request, 'kingadmin/news.html', locals())


class Newsadd(View):
    def get(self, request, *args, **kwargs):
        obj = NewForm()
        return render(request, 'kingadmin/newsadd.html', locals())

    def post(self, request, *args, **kwargs):
        obj = NewForm(request.POST, request.FILES)
        if obj.is_valid():
            new_obj = News.objects.create(**obj.cleaned_data)
            if obj.cleaned_data.get('img'):
                self.save_img(obj.cleaned_data.get('img'), new_obj.id)
            return redirect('/kingadmin/news/')
        return render(request, 'kingadmin/newsadd.html', locals())

    def save_img(self, img, cid):
        if img:
            News.objects.filter(id=cid).update(**{'img': img.name})
            img_path = os.path.join(BASE_DIR, 'status', 'upload', 'news', img.name)
            with open(img_path, 'wb') as f:
                for data in img.chunks():
                    f.write(data)


class NewsEdit(View):
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
        return render(request, 'kingadmin/newsadd.html', locals())

    def post(self, request, cid, *args, **kwargs):
        obj = NewForm(request.POST, request.FILES)
        if obj.is_valid():
            if not obj.cleaned_data.get('img'):
                del obj.cleaned_data['img']
            new_obj = News.objects.filter(id=cid).update(**obj.cleaned_data)
            if obj.cleaned_data.get('img'):
                self.save_img(obj.cleaned_data['img'])
            return redirect('/kingadmin/news/')
        print(obj.cleaned_data, 'cleaned_data')
        print(obj.errors)
        return render(request, 'kingadmin/newsadd.html', locals())

    def save_img(self, img):
        if img:
            img_path = os.path.join(BASE_DIR, 'status', 'upload', 'news', img.name)
            with open(img_path, 'wb') as f:
                for data in img.chunks():
                    f.write(data)


def delete_new(request,cid):
    News.objects.filter(id=cid).delete()
    return redirect('/kingadmin/news/')


def status_new(request,cid):
    status = request.GET.get('status', 0)
    News.objects.filter(id=cid).update(status=status)
    return redirect('/kingadmin/news/')