from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.

# def index(request):
#     return HttpResponse('欢迎访问！')


def index(request):
    return render(request, 'blog/index.html', context={'title': '我的博客首页', 'welcome': '欢迎访问我的博客'})

