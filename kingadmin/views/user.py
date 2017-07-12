from django.shortcuts import render, redirect, HttpResponse
from repository.models import User, Role, Role2User,UserInfo
from kingadmin.kingform import CompanyMemberForm,MemberFollowForm
from .baseview import BaseView
from utils.pages import Pagination
import json

class UserView(BaseView):

    def get(self,request,condition):
        p = request.GET.get('p')
        url = ''
        if condition in ('0','1','2'):
            user_list = UserInfo.objects.filter(status=condition)
        else:
            user_list = UserInfo.objects.all()
        page_obj = Pagination(user_list.count(), p, url, 10, 7)
        cm_list = user_list[page_obj.start:page_obj.end]
        return render(request,'kingadmin/user/user.html',locals())


class UserOperate(BaseView):

    def get(self, request,operate, cid,condition, *args , **kwargs):
        old_url = '/kingadmin/user/%s/'%condition
        # old_url = '/kingadmin/user'
        print(old_url)
        if hasattr(UserOperate,operate):
            func = getattr(UserOperate,operate)
            func(self, cid)
        return redirect(old_url)

    def msg(self,req, cid):
        pass

    def email(self, cid):
        pass

    def lock(self, cid):
        UserInfo.objects.filter(id=cid).update(status=2)

    def unlock(self, cid):
        UserInfo.objects.filter(id=cid).update(status=1)


class AdminView(BaseView):
    def get(self, request):
        admin_list = Role2User.objects.filter(role__id=2)
        return render(request, '', locals())


class RoleView(BaseView):
    def get(self,request):
        role_list = Role.objects.all()

        return render(request,'kingadmin/user/rolelist.html',locals())


class RoleEdit(BaseView):
    def post(self,request,cid):
        name = request.POST.get('name')
        data = {'status':True,'msg':'更新成功'}
        ret = Role.objects.filter(id=cid).update(name=name)
        if not ret:
            data['status'] = False
            data['msg'] = '更新失败'
        return HttpResponse(json.dumps(data))


class ActionView(BaseView):
    def get(self,request):
        role_list = Role.objects.all()

        return render(request,'kingadmin/user/rolelist.html',locals())