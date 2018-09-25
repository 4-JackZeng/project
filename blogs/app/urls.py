from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from app import views


urlpatterns =[
    #注册
    url(r'^register/',views.register,name='register'),
    #登录
    url(r'^login/',views.login,name='login'),
    #首页
    url(r'^index/',login_required(views.index),name='index'),
    #退出登录
    url(r'^back_login/',views.back_login,name='back_login'),
    #进入文章
    url(r'^article/',views.article,name='article'),
    #进入公告
    url(r'^notice/',views.notice,name='notice'),
    #进入评论
    url(r'^comment/',views.comment,name='comment'),
    #进入栏目
    url(r'^category/',views.category,name='category'),
    #进入友情链接
    url(r'^flink/',views.flink,name='flink'),
    #基本设置
    url(r'^setting/',views.setting,name='setting'),
    #阅读设置
    url(r'^readset/',views.readset,name='readset'),
    #进入管理用户
    url(r'^manage_user/',views.manage_user,name='manage_user'),
    #进入管理登录日志
    url(r'^loginlog/',views.loginlog,name='loginlog'),
    #增加文章
    url(r'^add_article/',views.add_article,name='add_article'),
    #修改文章
    url(r'^update_article/(?P<num>\d+)',views.update_article,name='update_article'),
    #删除文章
    url(r'^del_article/(?P<num>\d+)',views.del_article,name='del_article'),
    # url(r'^guanli',views.guanli,name='gunali'),
#进入前端登录页面
    url(r'^loginw/',views.loginw,name='loginw')
    # url(r'^release',views.release,name='release')

]