from django.shortcuts import render,HttpResponse
from django.views import View
from repository.models import *

class Index(View):

    def get(self,request):
        menu_list = Menu.objects.all()
        return render(request,'web/index.html',locals())

class Contactus(View):
    def get(self, request):
        pass


