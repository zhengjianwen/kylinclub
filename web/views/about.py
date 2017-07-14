from django.shortcuts import render,HttpResponse
from django.views import View
from repository.models import *


class Introduction(View):
    '''了解麒麟会'''
    def get(self,request):
        menu_list = Menu.objects.all()
        url = request.get_full_path()
        obj = ActivityClass.objects.filter(url=url).first()
        hd_list = ActivityClass.objects.filter(menu__id=3)
        left_menu = ActivityClass.objects.filter(menu__id=2)
        return render(request,'web/introduction.html',locals())

class ActivityWeb(View):
    '''了解麒麟会'''
    def get(self,request):
        menu_list = Menu.objects.all()
        url = request.get_full_path()
        obj = ActivityClass.objects.filter(url=url).first()
        hd_list = ActivityClass.objects.filter(menu__id=3)
        left_menu = ActivityClass.objects.filter(menu__id=2)
        activity_list = Activity.objects.all().order_by('-create_at')
        return render(request, 'web/activity.html', locals())
