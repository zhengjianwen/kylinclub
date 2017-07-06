#!/usr/bin/env python
# -*- coding=utf-8 -*-
import os,uuid,json
from kylinclub.settings import BASE_DIR
from django.shortcuts import render, redirect,HttpResponse


def upload_kindeditor_img(request):
    ret = {'error': 0, 'url': None, 'message': '上传成功'}
    if request.method == 'POST':
        print(request.FILES)
        file_obj = request.FILES.get('imgFile')
        if not file_obj:
            ret['error'] = 1
            ret['message'] = '没有内容'
        else:
            file_name = str(uuid.uuid4()) + file_obj.name
            file_path = os.path.join(BASE_DIR, 'status', 'upload', 'img', file_name)
            with open(file_path, 'wb') as f:
                for chunk in file_obj.chunks():
                    f.write(chunk)

            ret['url'] = '/static/upload/img/' + file_name


    return HttpResponse(json.dumps(ret))
