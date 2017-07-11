#!/usr/bin/env python
# -*- coding=utf-8 -*-
from django.shortcuts import render, redirect, HttpResponse
from repository.models import Carousel,Menu
from kingadmin.kingform import CarouselForm
from .baseview import BaseView
from utils.pages import Pagination


class CarouseView(BaseView):
    def get(self, request):
        menu_list = Menu.objects.all()
        return render(request, 'kingadmin/lunbo/carousel.html', locals())


class CarouseAdd(BaseView):
    title = '添加轮播图'

    def get(self, request, *args, **kwargs):
        obj = CarouselForm()
        return render(request, 'kingadmin/lunbo/carouseledit.html', locals())

    def post(self, request, *args, **kwargs):
        obj = CarouselForm(request.POST,request.FILES)
        if obj.is_valid():
            if obj.cleaned_data.get('img',0):
               path = self.save_img(obj.cleaned_data['img'], 'banner')
               obj.cleaned_data['img'] = path
            else:
                del obj.cleaned_data['img']
            Carousel.objects.create(**obj.cleaned_data)
            return redirect('/kingadmin/lunbo/')
        return render(request, 'kingadmin/lunbo/carouseledit.html', locals())


class CarouseEdit(BaseView):
    title = '编辑轮播图'

    def get(self, request, cid, *args, **kwargs):
        carousel_obj = Carousel.objects.filter(id=cid).first()
        in_form = {
            'weight': carousel_obj.weight,
            'status': carousel_obj.status,
            'orgid': carousel_obj.orgid,
            'title': carousel_obj.title,
            'content': carousel_obj.content,
            'url': carousel_obj.url,
            'img': carousel_obj.img,
        }
        obj = CarouselForm(initial=in_form)
        return render(request, 'kingadmin/lunbo/carouseledit.html', locals())

    def post(self, request, cid, *args, **kwargs):
        obj = CarouselForm(request.POST,request.FILES)
        if obj.is_valid():
            if obj.cleaned_data.get('img',0):
               path = self.save_img(obj.cleaned_data['img'], 'banner')
               obj.cleaned_data['img'] = path
            else:
                del obj.cleaned_data['img']
            Carousel.objects.filter(id=cid).update(**obj.cleaned_data)
            return redirect('/kingadmin/lunbo/')
        return render(request, 'kingadmin/lunbo/carouseledit.html', locals())


def carousedelete(request, cid):
    Carousel.objects.filter(id=cid).delete()
    return redirect('/kingadmin/mainset/')