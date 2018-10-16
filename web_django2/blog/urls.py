from django.conf.urls import url

from . import views
#web约定优于配置
urlpatterns = [
    # 配置了路由
    # 第一个参数是正则表达式，表示URI
    # 第二个是绑定一个函数，视图函数
    url(r"^index/$",views.index,name="index"),
    url(r"^index_3/$",views.index_3,name="index_3"),
    url(r"^login_3/$",views.login_3,name="login_3"),
    url(r"^register/$",views.register,name="register"),
    url(r"^add_user_3/$",views.add_user_3,name="add_user_3"),
    # url(r"^list/$",views.list,name="list"),
    url(r"^add_user/$",views.add_user,name="add_user"),
    # url(r"^delete_user/$",views.delete_user,name="delete_user"),
    url(r"^login/$", views.login, name="login"),
    url(r"^logout/$", views.logout, name="logout"),
    # url(r"^list_user/$",views.list_user,name="list_user"),
    url(r"^delete_user/(?P<user_id>\d+)/$", views.delete_user, name="delete_user"),
    url(r"^list_user/$", views.list_user, name="list_user"),
    url(r"^reg/$", views.reg, name="reg"),
    url(r"^show/(\d+)/$", views.show, name="show"),
    url(r"^(?P<u_id>\d+)/update/$", views.update, name="update"),

    url(r"^add_article/$", views.add_article, name="add_article"),
    url(r"^(?P<a_id>\d+)/delete_article/$", views.delete_article, name="delete_article"),
    url(r"^(?P<a_id>\d+)/update_article/$", views.update_article, name="update_article"),
    url(r"^(?P<a_id>\d+)/show_arcticle/$", views.show_arcticle, name="show_arcticle"),
    url(r"^self_article/$",views.self_article,name="self_article"),

    url(r"^code/$",views.code,name="code"),
    url(r"^(\w+)/checkusername/$", views.checkusername, name="checkusername"),
    # url(r"^ajax_hello/$", views.ajax_hello, name="ajax_hello"),

]
