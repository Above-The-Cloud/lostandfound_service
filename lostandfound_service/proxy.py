# -*- coding: utf-8 -*-
import requests
from django.http import HttpResponse

# 接收请求数据
def proxy(request):
    request.encoding='utf-8'
    g = request.GET
    r = requests.get(g["url"])
    return HttpResponse(r.text)