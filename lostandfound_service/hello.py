# -*- coding: utf-8 -*-
import requests
from django.http import HttpResponse

# 接收请求数据
def hello(request):
    return HttpResponse("hello")