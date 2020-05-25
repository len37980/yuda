#coding=utf-8
from django.shortcuts import render,redirect
from django.http import JsonResponse,HttpResponseRedirect
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
    uname=request.COOKIES.get('uname','')
    context={'title':'用户登陆','error_name':0,'error_pwd':0,'uname':uname,'upwd':''}
    return render(request,'df_user/login.html',context)
def login_handle(request):
    #接收请求信息
    post=request.POST
    uname=post.get('username')
    upwd=post.get('pwd')
    jizhu=post.get('jizhu',0) #如果记住密码这个选项没有被选中就不会提交，没有提交就GET不到jizhu的值，就使用0作为默认值
    #查询用户是否存在，这里用filter而不用get是因为用户有可能不存在，当用户不存在时get会报错，需要捕捉错误。filter侧返回一个空列表
    users=UserInfo.objects.filter(uname=uname)
    if len(users)==1:
        s1=sha1()
        s1.update(upwd.encode("utf8"))
        if s1.hexdigest()==users[0].upwd:
            red=HttpResponseRedirect('/user/userinfo/')
            #记住用户名
            if jizhu!=0:
                red.set_cookie('uname',uname)
            else:
                red.set_cookie('uname','',max_age=-1)
            #保存登陆信息
            request.session['user_id']=users[0].id
            request.session['user_name']=uname
            return red
        else:
            #密码错误
            context={'title':'用户登陆','error_name':0,'error_pwd':1,'uname':uname,'upwd':upwd}
            return render(request,'df_user/login.html',context)
    else:
        #用户不存在
        context={'title':'用户登陆','error_name':1,'error_pwd':0,'uname':uname,'upwd':upwd}
        return render(request,'df_user/login.html',context)


#检查用户是否存在
def register_exist(request):
    uname=request.GET.get('uname')
    count=UserInfo.objects.filter(uname=uname).count()
    return JsonResponse({'count':count})

#用户信息
def userinfo(request):
    return render(request,'df_user/user_center_info.html',{'title':'基本信息'})
#用户订单
def userorder(request):
    return render(request,'df_user/user_center_order.html',{'title':'订单信息'})
#收货地址
def usersite(request):
    return render(request,'df_user/user_center_site.html',{'title':'收货地址'})