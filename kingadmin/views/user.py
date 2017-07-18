from django.shortcuts import render, redirect, HttpResponse
from repository.models import User, Role, Role2User,UserInfo,Role2AdminMenuAction,MainMenu,AdminMenuAction
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
    '''用户验证'''
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
    '''角色编辑'''
    def post(self,request,cid):
        name = request.POST.get('name')
        data = {'status':True,'msg':'更新成功'}
        ret = Role.objects.filter(id=cid).update(name=name)
        if not ret:
            data['status'] = False
            data['msg'] = '更新失败'
        return HttpResponse(json.dumps(data))


class Role2UserView(BaseView):
    '''用户与角色关联函数'''
    def get(self,request,cid):
        sesion = session_key = request.session.session_key
        data = {'status': True, 'roleuser': None, 'user': None}
        qx_list = Role2User.objects.filter(role_id=cid).values_list('user__id', 'user__name')
        exclude_list = map(lambda x: x[0], list(Role2User.objects.all().values_list('user__id')))
        user_list = UserInfo.objects.all().exclude(user_id__in=exclude_list).values_list('id', 'name')
        data['roleuser'] = list(qx_list)
        data['user'] = list(user_list)
        return HttpResponse(json.dumps(data))

    def post(self, request, cid):
        data = {'status': True, 'msg':None}
        try:
            info_user_list = request.POST.getlist('user')
            info_user_list = list(map(lambda x: int(x), info_user_list))
            user_list = Role2User.objects.filter(role_id=cid).values('user')
            old_user = list(map(lambda x:x['user'],user_list))
            for u_id in info_user_list:
                if u_id not in old_user:
                    Role2User.objects.create(user_id=u_id,role_id=cid)
            del_list = set(old_user) - set(info_user_list)
            Role2User.objects.filter(user_id__in=del_list).delete()
        except Exception as e:
            data['status'] = False
            data['msg'] = '%s' % e
            print('erroe:',e)
        return HttpResponse(json.dumps(data))


class RoleActionView(BaseView):
    '''角色与权限设置'''
    def get(self,request,rid):
        role_obj = Role.objects.filter(id=rid).first()
        qx_list = MainMenu.objects.all()
        role_action = Role2AdminMenuAction.objects.filter(role_id=rid)
        role_action_ids = list(map(lambda x: x.rama_id, role_action))
        return render(request,'kingadmin/user/roletofunc.html',locals())

    def post(self,request,rid):
        role_obj = Role.objects.filter(id=rid).first()
        role_action = Role2AdminMenuAction.objects.filter(role=role_obj) # 获取角色下的所有权限对象
        role_action_ids = list(map(lambda x: x.rama_id, role_action))   # 获取所有权限的ids
        try:
            info_action = request.POST.getlist('role')
            info_action = list(map(lambda x: int(x), info_action))  # 新提交的权限id
            for i in info_action:
                if i not in role_action_ids:
                    Role2AdminMenuAction.objects.create(role=role_obj,rama_id=i)
            del_list = set(role_action_ids) - set(info_action)
            print('删除',del_list)
            Role2AdminMenuAction.objects.filter(role=role_obj,rama_id__in=del_list).delete()
        except Exception as e:
            print(e)
        return redirect('/kingadmin/user/roleaction/%s' % rid)


class ActionView(BaseView):
    '''权限管理'''
    def get(self,request):
        action_list = AdminMenuAction.objects.all()
        return render(request,'kingadmin/user/actionlist.html',locals())


def getuserlist(request):
    '''获取用户与角色关系'''
    sesion = session_key = request.session.session_key
    cid = request.GET.get('cid')
    data = {'status':True,'roleuser':None,'user':None}
    qx_list = Role2User.objects.filter(role_id=cid).values_list('user__id','user__name')
    exclude_list = map(lambda x:x[0],list(Role2User.objects.all().values_list('user__id')))
    user_list = UserInfo.objects.all().exclude(user_id__in=exclude_list).values_list('id','name')
    data['roleuser'] = list(qx_list)
    data['user'] = list(user_list)
    return HttpResponse(json.dumps(data))

