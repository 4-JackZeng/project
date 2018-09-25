from django.db import models


class Person(models.Model):
    # 创建人员表
    name=models.CharField(max_length=8,unique=True,verbose_name='人员姓名')
    password=models.CharField(max_length=200,unique=True,verbose_name='密码')
    age=models.IntegerField(unique=True,null=True,verbose_name='密码')
    sex=models.BooleanField(default=1,verbose_name='性别')
    create_time=models.DateTimeField(auto_now_add=True,verbose_name='创建时间')
    operate_time=models.DateTimeField(auto_now=True,verbose_name='修改时间')

    class Meta:
        db_table='user'


class Article(models.Model):
    # 创建文章表
    keywords = models.CharField(max_length=50, unique=True, verbose_name='关键字')
    describe = models.CharField(max_length=100, unique=True, verbose_name='描述')
    content = models.TextField(null=True,verbose_name='内容')
    icon = models.ImageField(upload_to='upload', null=True, verbose_name='图片')
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    operate_time = models.DateTimeField(auto_now=True, verbose_name='修改时间')


    class Meta:
        db_table='article'


class Tag(models.Model):
    # 创建标签表
    t_name=models.CharField(max_length=200,unique=True,null=True,verbose_name='标签名')
    class Meta:
        db_table='tag'


class Category(models.Model):
    # 创建分类表
    c_name=models.CharField(max_length=20,unique=True,null=True,verbose_name='分类名')
    class Meta:
        db_table='category'







