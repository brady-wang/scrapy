# -*- coding: UTF-8 -*-
from django.http import HttpResponse
from django.shortcuts import render


def hello(request):
    content = {}
    content['hello'] = "hello world"
    content['title'] = "标题"
    return render(request,'hello.html',content)
