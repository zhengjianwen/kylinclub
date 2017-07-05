from django.shortcuts import render,redirect
from django.views import View


class Login(View):

    def get(self,request):

        return render(request, 'kingadmin/login.html', locals())


class Logout(View):

    def get(self,request):

        return redirect('/')