from django.conf.urls import url,include
from . import views

app_name='df_user'
urlpatterns=[
    url(r'^$',views.login,name='login'),
    url(r'^register/$',views.register, name='register' ),
    url(r'^register_handle/$',views.register_handle,name='register_handle'),
    url(r'^login/$',views.login,name='login'),
    url(r'^login_handle/$',views.login_handle,name='login_handle'),
    url(r'^register_exist/$',views.register_exist,name='register_exist'),

    url(r'^userinfo/$',views.userinfo,name='userinfo'),
    url(r'^userorder/$',views.userorder,name='userorder'),
    url(r'^usersite/$',views.usersite,name='usersite'),
    
]