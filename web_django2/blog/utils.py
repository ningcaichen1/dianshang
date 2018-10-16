import random,string
import hashlib
import hmac
import logging
import re
from PIL import Image,ImageDraw,ImageFont,ImageFilter
                # 图片、画布、图片（上的）字体、给图片加滤镜（模糊该图片，使机器更加难以识别~）
from django.conf import  settings
from django.shortcuts import  render

# 使用正则清除HTML标签
def clear_html_re(content):
    s_content = re.sub(r"</?(.+?)>", "", content)
    logging.warning(s_content)
    return s_content


# 一个判断用户是否登录的装饰器
def require_login(fn):
    def inner(request, *args, **kwargs):
        if request.session.has_key("loginUser"):
            logging.warning("该用户已经登录，视图函数正常访问")
            return fn(request, *args, **kwargs)
        else:
            logging.warning("当前操作需要登录才能执行，请先登录")
            return render(request, "blog/login.html", {"msg": "当前操作必须登录，请先登录系统"})
    return inner



# 获取一个随机字符串，4位的
def getRandomChar(count=4):
    # 生成随机字符串
    # string模块包含各种字符串，以下为小写字母、大写字母加数字    （a~z,0~9的字符串）
    ran = string.ascii_lowercase + string.ascii_uppercase + string.digits
    char = ''
    for i in range(count):
        char += random.choice(ran)
    return char


# 返回一个随机的RGB颜色
def getRandomColor():
    return (random.randint(50,150),random.randint(50,150),random.randint(50,150))


def create_code():
    # 创建图片，模式，大小，背景色
    img = Image.new('RGB', (120,30), (255,255,255))
    #创建画布
    draw = ImageDraw.Draw(img)
    # 设置字体
    font = ImageFont.truetype('arial.ttf', 25)

    code = getRandomChar()
    # 将生成的字符画在画布上
    for t in range(4):
        draw.text((30*t+5,0),code[t],getRandomColor(),font)
#[5,30]、[35,60]、[65,90]、[95,120]（value值）字体颜色（随机颜色，增加扫描难度）
    # 生成干扰点
    for _ in range(random.randint(0,200)):
        # 位置，颜色
        draw.point((random.randint(0, 120),
random.randint(0, 30)),fill=getRandomColor())

    # 使用模糊滤镜使图片模糊
    # img = img.filter(ImageFilter.BLUR)
    # 保存
    # img.save(''.join(code)+'.jpg','jpeg')
    return img,code

if __name__ == '__main__':
    print(create_code())


#hash加密
def hash_by_md5(pwd):
    md5 = hashlib.md5(pwd.encode("utf-8"))
    md5.update(settings.MD5_SALT.encode("utf-8"))
    return md5.hexdigest()


#hash加密，这种方法使用了对称加密和hash，安全性更高
def hmac_by_md5(pwd):
    return hmac.new(pwd.encode('utf-8'),settings.MD5_SALT.encode("utf-8"), "MD5").hexdigest()


















