from django.db import models
from datetime import datetime

#富文本一引入
# from tinymce.models import HTMLField

#富文本框二引入
from DjangoUeditor.models import UEditorField

#第一种方法：使用类方法操作
    # @classmethod
    # def create_user(cls,username,password,age,email):  #cls代指的上面的User类
    #     user = cls(username = username,password = password,age = age,email = email)
    #     return user


#第二种方法：使用面向对象操作：
#创建一个管理  上面 User的类   必须继承 Manager类
# class UserManager(models.Manager):
#
#     def add_user(self,nickname,password,tel):
#         return self.create(nickname = nickname,password = password,tel = tel)
        #create  本身带有save函数（功能）


# class User(models.Model):
#     id = models.AutoField(primary_key=True)
#     # username = models.CharField(max_length=50,verbose_name="用户名称")
#     password = models.CharField(max_length=100,verbose_name="用户密码")
#     age = models.IntegerField(default=18,verbose_name="用户年龄")
#     nickname = models.CharField(max_length=255,verbose_name="用户昵称")
#     tel = models.IntegerField(verbose_name="手机号码")
#     birthday = models.DateTimeField(default=datetime.now(),verbose_name="用户生日")
#     # email = models.EmailField(max_length=255,verbose_name="用户邮箱")
#     #默认是0，表示男生，1表示女生
#     # gender = models.BooleanField(default=0)
#     class Meta:
#         ordering = ["id"]

class User(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20,verbose_name="用户名称")
    password = models.CharField(max_length=50,verbose_name="用户密码")
    age = models.IntegerField(default=18,verbose_name="用户年龄")
    nickname = models.CharField(max_length=100,verbose_name="用户昵称")
    tel = models.IntegerField(default=0,verbose_name="手机号码")
    birthday = models.DateTimeField(default=datetime.now(),verbose_name="用户生日")

    # header = models.CharField(max_length=255,default="/static/img/1.png",verbose_name="用户头像")
    #header = models.FileField()
    header = models.ImageField(upload_to='static/img/headers/', default="static/img/1.png", verbose_name="用户头像")

    # email = models.EmailField(max_length=255,verbose_name="用户邮箱")
    #默认是0，表示男生，1表示女生
    # gender = models.BooleanField(default=0)
    class Meta:
        ordering = ["id"]

    def __str__(self):
        return  self.nickname


class Article(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=50, verbose_name="文章标题")
    # content = models.TextField()

    # 富文本一
    # content = HTMLField()

    # 富文本二
    content = UEditorField()

    publishTime = models.DateTimeField(auto_now_add=True)
    modifyTime = models.DateTimeField(auto_now=True)

    # 外键
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        ordering = ['-publishTime']


    #管理UserManager类
    # um = UserManager()
    #
    # def __str__(self):
    #     return self.nickname

# class Meta:
#     db_table = "t_user"

#第一种方法：使用类方法操作
    # @classmethod
    # def create_user(cls,username,password,age,email):  #cls代指的上面的User类
    #     user = cls(username = username,password = password,age = age,email = email)
    #     return user