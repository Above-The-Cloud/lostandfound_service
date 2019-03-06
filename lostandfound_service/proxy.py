# -*- coding: utf-8 -*-
import requests
from django.http import HttpResponse

# 接收请求数据
def proxy(request):
    request.encoding='utf-8'
    g = request.GET
    if "params" in g:
        r = requests.get(g["url"], params=g["params"])
    else:
        r = requests.get(g["url"])
    hr = HttpResponse(r.text)
    hr.__setitem__("access-Control-Allow-Origin", "*")
    return hr