#!/usr/bin/env python
# -*- coding=utf-8 -*-
from django.views import View
from kylinclub.settings import BASE_DIR
import os,time
from hashlib import md5


class BaseView(View):

    def save_img(self, img, pathname):
        if img:

            filename = str(self.name_md5()) +img.name
            print('-->正在写入文件', filename)
            img_path = os.path.join(BASE_DIR, 'status', 'upload', pathname, filename)
            with open(img_path, 'wb') as f:
                for data in img.chunks():
                    f.write(data)
                print('-->写入文件完成',filename)
            return '%s/%s' % (pathname, filename)

    def name_md5(self):
        m = md5()
        t = str(time.time()).encode("utf-8")
        m.update(t)  # 需要转换成字节类型
        return m.hexdigest()