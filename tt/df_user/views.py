#coding=utf-8
from django.shortcuts import render,redirect
from django.http import JsonResponse
from hashlib import sha1
from df_user.models import *

#用户注册
def register(request):
    return render(request,'df_user/register.html',{'title':'用户注册'})

def register_handle(request):
    #接收用户输入
    post=request.POST
    uname=post.get('user_name')
    upwd=post.get('pwd')
    ucpwd=post.get('cpwd')
    uemail=post.get('email')
    #判断两次密码是否一样
    if upwd != ucpwd:
        return redirect('/user/register/')
    #密码加密
    s1=sha1()
    s1.update(upwd.encode("utf8")) #注：新版需要指定字符串的编码
    upwd_sha=s1.hexdigest()
    #创建用户对像
    user=UserInfo()
    user.uname=uname
    user.upwd=upwd_sha
    user.uemail=uemail
    user.save()
    #注册成功,转到登陆页面
    return redirect('/user/login/')
def login(request):
    return render(request,'df_user/login.html')

#检查用户是否存在
def register_exist(request):
    uname=request.GET.get('uname')
    count=UserInfo.objects.filter(uname=uname).count()
    return JsonResponse({'count':count})

#用户信息
def userinfo(request):
    return render(request,'df_user/user_center_info.html')
#用户订单
def userorder(request):
    return render(request,'df_user/user_center_order.html')
#收货地址
def usersite(request):
    return render(request,'df_user/user_center_site.html')