from django.contrib import admin

# Register your models here.

from . import models


class UserAdmin(admin.ModelAdmin):
    #列表时显示的操作
    list_display = ["name","nickname","age","birthday"]

    #列表时过滤字段
    list_filter = ("name","age")

    #进行分页，每页两行数据
    # list_per_page = 2

    #可编辑的（可修改）
    list_editable = ["nickname","age"]

    #指定可以点击进去查看的属性
    # list_display_links = ["age","nickname"]

    #修改增加用户时允许出现的选项 & 与下面的语句只能出现一个
    fields = ["name","ninckname","age"]

    #与上面的修改的同一个东西
    #分组功能
    # fieldsets = [
    #     ("base",{"fields":{"age","header"}}),
    #     ("other",{"fields":{"name","nickname"}}),
    # ]

admin.site.register(models.User, UserAdmin)
admin.site.register(models.Article)