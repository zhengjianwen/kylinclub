#!/usr/bin/env python
# -*- coding=utf-8 -*-
from django.views import View
from kylinclub.settings import BASE_DIR
import os


class BaseView(View):

    def save_img(self, img, pathname):
        if img:
            img_path = os.path.join(BASE_DIR, 'status', 'upload', pathname, img.name)
            with open(img_path, 'wb') as f:
                for data in img.chunks():
                    f.write(data)