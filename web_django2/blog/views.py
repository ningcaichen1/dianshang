from django.http import HttpResponseRedirect, HttpResponse,JsonResponse
from django.shortcuts import render, redirect,reverse

from . import utils

#引入函数装饰器
from .utils import require_login

from io import BytesIO
import uuid
from . import models

from django.core.cache import cache
from . import cache_utils

from django.views.decorators.csrf import csrf_exempt

#装饰器， 只能使用get请求，只能传递参数，只能使用post请求，只能使用https连接
from django.views.decorators.http import require_GET, require_http_methods, require_POST, require_safe
from django.forms.models import model_to_dict
from django.core.serializers import serialize

import math
from django.conf import settings

#引入django自带分页模块
from django.core.paginator import Paginator


def index_3(request):
    return render(request,"blog/index_3.html", {})


def login_3(request):
    # users = models.User.objects.all()
    return render(request,"blog/1login登录页面.html",{})

def add_user_3(request):
    return render(request, "blog/2register注册页面.html", {})

def register(request):
    if request.method == "GET":
        return render(request, "blog/2register注册页面.html", {"msg":"请填写您的信息"})
    elif request.method == "POST":
        #接受页面传来的参数
        try :
            nickname =request.POST.get("nickname")
            # print(nickname)
            tel = request.POST.get("tel")
            password = request.POST.get("password").strip()
            # print(password)
            confirmpwd = request.POST.get("confirmpwd").strip()

            # 数据校验
            if len(nickname) < 1:
                return render(request,"blog/2register注册页面.html",{"msg": "用户名称不能为空！！"})
            if len(password) < 8:
                return render(request,"blog/2register注册页面.html",{"msg": "密码长度不能小于8位！！"})
            if password != confirmpwd:
                return render(request,"blog/2register注册页面.html",{"msg": "两次密码不一致！！"})

            # # 判断用户名称是否重复
            # nick = models.User.objects.filter(nickname = nickname)
            # if nick in nickname:
            #     return render(request,"blog/2register注册页面.html",{"msg":"重复用户名 ! !"})

            # 保存数据
            user = models.User(nickname=nickname, password=password, tel = tel)
            user.save()
            return render(request,"blog/2register注册页面.html",{"msg": "恭喜您，注册成功！！"})
        except :
            return render(request,"blog/2register注册页面.html",{"msg": "对不起，注册失败，请重新注册！！"})

def reg(request):
    if request.method == "GET":
        return render(request, "blog/add_user.html", {"msg": "请认真填写如下选项"})
    elif request.method == "POST":
        # 接受参数
        try:
            username = request.POST["username"].strip()
            password = request.POST.get("password").strip()  # .getlist()
            confirmpwd = request.POST.get("confirmpwd").strip()
            nickname = request.POST.get("nickname", None)
            avatar = request.FILES.get("avatar", 'static/img/1.png')

            code = request.POST['code']

            mycode = request.session["code"]
            if code.upper() != mycode.upper():
                return render(request, "blog/add_user.html", {"msg": "验证码错误，请重新输入！！"})

            # 删除session中验证码
            del request.session["code"]

            # 数据校验
            if len(username) < 1:
                return render(request, "blog/add_user.html", {"msg": "用户名称不能为空！！"})
            if len(password) < 6:
                return render(request, "blog/add_user.html", {"msg": "密码长度不能小于6位！！"})
            if password != confirmpwd:
                return render(request, "blog/add_user.html", {"msg": "两次密码不一致！！"})
            # 用户名称是否重复
            try:
                user = models.User.objects.get(name=username)
                return render(request, "blog/add_user.html", {"msg": "该用户名称已经存在，请重新填写！！"})
            except:
                # 先对密码加密，之后在保存
                password = utils.hmac_by_md5(password)

                user = models.User(name=username, password=password, nickname=nickname, header=avatar)
                user.save()
                return render(request, "blog/add_user.html", {"msg": "恭喜您，注册成功！！"})

                # 保存数据
                # try:
                    # avatar = request.FILES['avatar']
                    # 保存图片
                    # path = "static/img/headers/" + uuid.uuid4().hex + avatar.name
                    # with open(path, "wb") as f:
                    #     for file in avatar.chunks():
                    #         f.write(file)

                    # user = models.User(name=username, password=password, nickname=nickname, header=avatar)
                #     user.save()
                #     return render(request, "blog/add_user.html", {"msg": "恭喜您，注册成功！！"})
                # except Exception as e:
                #     print(e)
                #     user = models.User(name=username, password=password, nickname=nickname)
                #     user.save()
                #     return render(request, "blog/add_user.html", {"msg": "恭喜您，注册成功！！"})
        except:
            return render(request, "blog/add_user.html", {"msg": "对不起，用户名称不能为空！！"})


    # if request.method == "GET":
    #     return render(request, "blog/add_user.html", {"msg": "请认真填写如下选项"})
    # elif request.method == "POST":
    #     # 接受参数
    #     try:
    #         username = request.POST["username"].strip()
    #         password = request.POST.get("password").strip()  # .getlist()
    #         confirmpwd = request.POST.get("confirmpwd").strip()
    #         nickname = request.POST.get("nickname",None)
    #
    #         # 数据校验
    #         if len(username) < 1:
    #             return render(request, "blog/add_user.html", {"msg": "用户名称不能为空！！"})
    #         if len(password) < 6:
    #             return render(request, "blog/add_user.html", {"msg": "密码长度不能小于6位！！"})
    #         if password != confirmpwd:
    #             return render(request, "blog/add_user.html", {"msg": "两次密码不一致！！"})
    #         # 用户名称是否重复
    #         try:
    #             user = models.User.objects.get(name=username)
    #             return render(request, "blog/add_user.html", {"msg": "用户名重复，请重新注册！"})
    #         except:
    #             # 保存数据
    #             user = models.User(name=username, password=password, nickname=nickname)
    #             user.save()
    #             return render(request, "blog/add_user.html", {"msg": "恭喜您，注册成功！！"})
    #     except:
    #         return render(request, "blog/add_user.html", {"msg": "对不起，用户名称不能为空！！"})

# def add_user(request):
    # 首先需要接受页面传递过来的参数
    # nickname= "zhangsan"
    # password = "123456"
    # tel = "15896910029"
    # try:
    #     # 第一种方式，使用类方法的方式完成数据的操作
    #     user = models.User.create_user(username=username, password=password, age=age, email = email)
    #     user.save()
    #     return HttpResponse("<h2>用户添加成功!!!</h2>")
    # except:
    #     return HttpResponse("<h2>对不起，用户添加失败！！！</h2>")

    # try:
    #     # 第三种，使用面向过程的方式实现,最简单的一种方式，第一种是第三种的复杂版；
    #     #为了快速可以经常使用，不过在面向对象中应该有一个单独的类对它进行操作
    #     # 因为我们model类继承了Model类，在Model类中有大量方法和属性
    #     # user = models.User(username=username, password=password, age=age, email=email)
    #     # user.save()
    #     return HttpResponse("<h2>用户添加成功！！！</h2>")
    # except:
    #     return HttpResponse("<h2>对不起，用户添加失败！！！</h2>")
    # try:
    #     # 第二种方式，面向对象实现；
    #     user = models.User.um.add_user(nickname = nickname, password=password,tel = tel)
    #     print(user.id, user.nickname, user.password, user.tel)
    #     return HttpResponse("<h2>用户添加成功！！！</h2>")
    # except:
    #     return HttpResponse("<h2>对不起，用户添加失败！！！</h2>")

def index(request):
    articles = cache_utils.getAllArticle()
    # 第一种分页的实现，我们自己手写实现
    pageSize = int(request.GET.get("pageSize", settings.PAGE_SIZE))
    pageNow = int(request.GET.get("pageNow", 1))

    allCount = len(articles)
    pageCount = math.ceil(allCount / pageSize)

    # queryset 有延迟加载的效果
    page = articles[(pageNow - 1)*pageSize:pageNow*pageSize]

    # print(page)
    print(pageNow)
    print(pageCount)
    print(pageSize)

    # 构造一个循环器，目前是为了页面上循环链接
    page_range = range(1, pageCount+1)
    return render(request, "blog/index.html", {"articles": page, "page_range": page_range,\
                                               "pageNow": pageNow, "pageSize": pageSize,\
                                               "allCount": allCount, "pageCount": pageCount})
    # 第二种分页 使用Django自带的分页器，首先构建一个Paginator对象
    # paginator = Paginator(articles, pageSize)
    # page = paginator.page(pageNow)
    #
    # return render(request, "blog/index1.html", {"page": page, "pageSize": pageSize})



    # return render(request, "blog/index.html", {"articles": articles})



def add_user(request):
    return render(request, "blog/add_user.html", {})


@require_login
def delete_user(request, user_id):
    # u_id = request.GET["id"]
    user = models.User.objects.get(pk=user_id)
    user.delete()
    # users = models.User.objects.all()
    # return render(request, "blog/user_list.html", {"msg": "删除用户成功！！", "users": users})
    # return HttpResponseRedirect("/blog/list_user/")
    return redirect("blog:list_user")


@require_login
def list_user(request):
    users = models.User.objects.all()
    return render(request, "blog/user_list.html",{"users": users})

@require_login
def show(request, u_id):
    user = models.User.objects.get(pk=u_id)
    return render(request, "blog/show.html", {"user": user})

@require_login
def update(request, u_id):
    if request.method == "GET":
        user = models.User.objects.filter(id=u_id).first()
        return render(request, "blog/update.html", {"user": user})
    else:
        nickname = request.POST["nickname"]
        age = request.POST['age']
        password = request.POST['password']

        # 先对密码加密，之后在保存
        password = utils.hmac_by_md5(password)

        # header = request.POST.get("avatar",'static/img/1.png')
        avatar = request.FILES.get("avatar", 'static/img/1.png')
        # 数据校验

        # 如何修改？？？？？？？？？？
        # 第一步，获取用户
        user = models.User.objects.get(pk=u_id)
        # 第二步，修改值
        user.age = age
        user.nickname = nickname
        user.password = password
        user.header = avatar
        # 第三步， 保存
        user.save()

        # try:
        #     del request.session["loginUser"]
        # finally:
        #     return redirect(reverse("blog:login"))


        # return redirect("/blog/show/" + str(u_id) + "/")


        return redirect(reverse("blog:show", args=(u_id,)))



        # return HttpResponse(file.getvalue(), "image/png")

login_error = 0
def login(request):
    """
    登录的视图函数，完成用户登录功能
    :param request: 请求头对象
    :return:
    """
    global login_error
    if request.method == "GET":
        return render(request, "blog/login.html", {"msg": "请登录"})
    elif request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        # 完善验证码
        if login_error>2:
            code = request.POST["code"]

            mycode = request.session["code"]
            if code.upper() != mycode.upper():
                return render(request, "blog/login.html", {"msg": "验证码错误，请重新输入！！"})

            # 删除session中验证码
            del request.session["code"]

        try:
            password = utils.hmac_by_md5(password)
            user = models.User.objects.get(name=username, password=password)
            # 使用session来记录登录用户的信息
            request.session["loginUser"] = user
            #使用cookie记住用户名称
            response = redirect(reverse("blog:index"))
            #cookie不能存储中文
            response.set_cookie("username",user.name,max_age=3600 * 24 * 14)
            return response
            # return redirect(reverse("blog:index"))
        except:
            login_error+=1
            return  render(request, "blog/login.html", {"login_error": login_error,"msg": "登录失败，请重新登录！！"})


def logout(req):
    try:
        del req.session["loginUser"]
    finally:
        return redirect(reverse("blog:index"))


@require_login
def add_article(request):
    if request.method == "GET":
        return render(request, "blog/add_article.html", {"msg": "请认真填写如下选项"})
    else:
        title = request.POST["title"]
        content = request.POST["content"]
        try:
            author = request.session["loginUser"]

            # 验证
            article = models.Article(title=title, content=content, author=author)
            article.save()

            #将缓存重新更新
            cache_utils.getAllArticle(ischange=True)

            return redirect(reverse("blog:show_arcticle", kwargs={"a_id": article.id }))
        except:
            return redirect(reverse("blog:login",))


@require_login
def delete_article(request, a_id):
    at = models.Article.objects.get(pk=a_id)
    at.delete()
    return redirect(reverse("blog:index"))


@require_login
def update_article(request, a_id):
    at = models.Article.objects.get(pk=a_id)
    if request.method == "GET":
        return render(request, "blog/update_at.html", {"article": at})
    else:
        title = request.POST["title"]
        content = request.POST["content"]
        at.title = title
        at.content = content
        at.save()
        return redirect(reverse("blog:show_arcticle", kwargs={"a_id": a_id}))


@require_login
def show_arcticle(request, a_id):
    at = models.Article.objects.get(pk=a_id)
    return render(request, "blog/show_at.html", {"article": at})


@require_login
def self_article(request):
    #第一种方法（直接打印出页面--不推荐）
     author = request.session["loginUser"]
     # print(dir(author))
     #第二种方法
     articles = models.Article.objects.filter(author=author)
     return  render(request, "blog/show_one.html",{"articles":articles})



def code(request):
    img, code = utils.create_code()
    # 首先需要将code保存到session中
    request.session['code'] = code
    # 返回图片
    file = BytesIO()
    img.save(file, 'PNG')

    return HttpResponse(file.getvalue(), "image/png")


@require_POST
# @csrf_exempt # 这个装饰器，表示装饰者的函数忽略csrf验证
# @require_http_methods("GET", "POST")
def ajax_hello(request):
    id = request.POST["id"]
    article = models.Article.objects.get(pk=id)
    # msg = {
    #     "id": user.id,
    #     "uname": user.name,
    #     "unickname": user.nickname,
    #     "uage": user.age
    # }
    # JsonResponse 返回一个字段对象，会自动完成dict--> json的转换
    return JsonResponse(model_to_dict(article))
    # HttpResponse返回的是字符串
    # return HttpResponse(msg)

    # jqueryset djang考虑到大家需要传输，提供了一个序列化
    # ats = models.Article.objects.all()
    # return HttpResponse(serialize("json", ats))


def checkusername(request, username):
    qs = models.User.objects.filter(name=username)
    if len(qs) > 0:
        return JsonResponse({"msg": "该用户名已经存在，请重新输入！！", "success": False})
    else:
        return JsonResponse({"msg": "恭喜您，用户名可用", "success": True})
