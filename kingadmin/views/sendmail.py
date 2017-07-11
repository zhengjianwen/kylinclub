from django.core.mail import send_mail
from django.shortcuts import render, redirect,HttpResponse


def sendmail(request):
    try:
        send_mail('麒麟会欢迎你2017',
                  '欢迎注册麒麟会网址',
                  'member@kylinclub.org',
                    ['574601624@qq.com',], fail_silently=True)
        return HttpResponse('发送成功')
    except Exception as e:
        return HttpResponse('%s'%(e))