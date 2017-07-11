from django.shortcuts import render, redirect, HttpResponse
from repository.models import CompanyMember, MemberFollow
from kingadmin.kingform import CompanyMemberForm,MemberFollowForm
from .baseview import BaseView
from utils.pages import Pagination
import json


class CompanyMemberView(BaseView):
    def get(self,request):
        p = request.GET.get('p')
        data = request.GET.get('data')
        m_obj = MemberFollowForm()
        obj = CompanyMemberForm()
        url = ''
        if data in ["0","4","5"] :
            cm_list = CompanyMember.objects.filter(status=data)
        else:
            cm_list = CompanyMember.objects.filter(status__in=(1,2,3))
        page_obj = Pagination(cm_list.count(),p,url,10,7)
        cm_list = cm_list[page_obj.start:page_obj.end]
        return render(request,'kingadmin/company/company.html', locals())

def companystatus(request):
    cid = request.POST.get('cid')
    status = request.POST.get('status')
    data = {'status': 1, 'msg': None}
    try:
        print('===>',cid,status)
        CompanyMember.objects.filter(id=cid).update(status=int(status))
    except Exception as e:
        data['status'] = 0
        data['msg'] = '执行错误'

    return HttpResponse(json.dumps(data))


def follow(request):
    data = {'status':0,'msg':None}
    obj = MemberFollowForm(request.POST)
    if obj.is_valid():
        MemberFollow.objects.create(**obj.cleaned_data)
        data['status'] = 1
    return HttpResponse(json.dumps(data))