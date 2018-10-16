"""web_django2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib import admin

#
import xadmin
from xadmin.plugins import xversion
xadmin.autodiscover()
xversion.register_models()


urlpatterns = [
    #如果不再使用默认的admin后台，可以注释掉
    url(r'^admin/', admin.site.urls),
    # 将子路由引入到根路由中(在一级路由中配置了一个二级路由)
    #namespace 是由name属性进行路由反解析
    url(r'^blog/', include("blog.urls",namespace="blog")),

    #为富文本框二上传文件配置路由
    url(r'^ueditor/', include('DjangoUeditor.urls')),

    url(r'^xadmin/', xadmin.site.urls),
]
