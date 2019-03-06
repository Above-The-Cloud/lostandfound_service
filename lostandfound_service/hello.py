# -*- coding: utf-8 -*-
import requests
from django.http import HttpResponse

# 接收请求数据
def hello(request):
     hr = HttpResponse("hello")
     hr.__setitem__("access-Control-Allow-Origin","*")
     return hr