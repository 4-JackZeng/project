from django.contrib import auth
from django.contrib.auth.models import User
from django.core.paginator import Paginator
from django.http import HttpResponseRedirect,HttpResponse
from django.shortcuts import render
from django.urls import reverse
from app.models import  Article


from app.forms import UserForm,UserloginForm,Textfrom
# Create your views here.
def register(request):
    if request.method == 'GET':
        return render(request,'register.html')
    if request.method == 'POST':
        #校验页面中传递的参数，是否填写完整
        form = UserForm(request.POST)
        if form.is_valid():
            #获取校验后的用户名和密码
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            User.objects.create_user(username=username,password=password)
            # return  render(request,'register.html')
            # else:
            #     return render(request,'register.html')
            #实现跳转
            return HttpResponseRedirect(reverse('app:login'))
        else:
            return render(request,'register.html',{'form':form})

def login(request):
    if request.method == 'GET':
        return  render(request,'login.html')

    if request.method == 'POST':
            #表单验证,用户名和密码是否填写，校验用户名是否注册
        form = UserloginForm(request.POST)
        # is_valid():判断表单是否验证通过
        if form.is_valid():
            user = auth.authenticate(username=form.cleaned_data['username'],
                                     password=form.cleaned_data['password'])
            if user:
                #用户名和密码是正确的
                #login登录
                auth.login(request,user)
                # return HttpResponseRedirect(reverse('app:index'))

                return render(request,'index.html',{'form':form})
            else:
                #密码不正确
                pass
                return render(request,'login.html',{'error':'密码错误'})


        else:
            return render(request,'login.html',{'form':form})


def index(request):
    if request.method == 'GET':
        message = User.objects.last()
        return render(request,'index.html')
    if request.method == 'POST':
        pass


def back_login(request):
    if request.method == 'GET':
        return  HttpResponseRedirect(reverse('app:login'))


def article(request):
    if request.method == 'GET':
        #获取表单信息
        form = UserloginForm(request.POST)
        text = Article.objects.all()
        # return HttpResponseRedirect(reverse('app:article'))
        return render(request,'article.html',{'text_content':text,'form':form})


def notice(request):
    if request.method == 'GET':
        return  render(request,'notice.html')


def comment(request):
    if request.method == 'GET':
        return  render(request,'comment.html')


def category(request):
    if request.method == 'GET':
        return  render(request,'category.html')


def flink(request):
    if request.method == 'GET':
        return  render(request,'flink.html')


def setting(request):
    if request.method == 'GET':
        return  render(request,'setting.html')


def readset(request):
    if request.method == 'GET':
        return  render(request,'readset.html')


def manage_user(request):
    if request.method == 'GET':
        return  render(request,'manage-user.html')


def loginlog(request):
    if request.method == 'GET':
        return  render(request,'loginlog.html')


def add_article(request):
    if request.method == 'GET':
        return  render(request,'add-article.html')
    if request.method == 'POST':
        text = Textfrom(request.POST,request.FILES)
        if text.is_valid():
            #获取文本类容
            title = text.cleaned_data['title']
            keywords = text.cleaned_data['keywords']
            describe = text.cleaned_data['describe']
            content = text.cleaned_data['content']
            #添加文章到数据库中
            Article.objects.create(title=title,keywords=keywords,describe=describe,content=content,
                                      icon=request.FILES.get('image'))
            return HttpResponseRedirect(reverse('app:article'))


def update_article(request,num):
    if request.method == 'GET':
        #接收html的id传参
        text = Article.objects.filter(id=num)
        return  render(request,'update-article.html',{'text_content':text})
    if request.method == 'POST':

        text = Textfrom(request.POST, request.FILES)
        if text.is_valid():
            # 获取文本类容
            title = text.cleaned_data['title']
            keywords = text.cleaned_data['keywords']
            describe = text.cleaned_data['describe']
            content = text.cleaned_data['content']
            #修改文章信息
            Article.objects.update(title=title, keywords=keywords, describe=describe, content=content)
            return HttpResponseRedirect(reverse('app:article'))


def del_article(request,num):
    if request.method == 'GET':
        # 获取文章对象
        text = Article.objects.filter(id=num)
        # 删除文章
        text.delete()
        return HttpResponseRedirect(reverse('app:article'))

def loginw(request):
    if request.method == 'GET':
        text = Article.objects.all()
        # 实现分页功能
        page_number = int(request.GET.get('page', 1))
        paginator = Paginator(text, 4)
        # 获取某一个的信息
        page = paginator.page(page_number)
        return render(request,'indexw.html',{'text_content':text,'page':page})