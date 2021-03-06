"""
Django settings for web_django2 project.

Generated by 'django-admin startproject' using Django 1.11.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '5=w)jdub$t9%qy5em6f-424p7gah&_u0tjw#k5lq(ds0*1xg12'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'blog',
    #富文本框一：
    # 'tinymce',
    #富文本框二：
    'DjangoUeditor',
    #xadmin,
    'xadmin',
    'crispy_forms',
    'reversion',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'web_django2.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, "templates")],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'web_django2.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME':"db_py1807b",
        # 'NAME':"db_py1807a",
        'USER':'root',
        'PASSWORD':'123456',
        'CHARSET':'utf8',
        'HOST':'localhost',
        'PORT':3306,
    }
}


# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'zh-Hans'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

STATIC_URL = '/static/'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR,"static")
]

#session存储对象前会自动调用该模块进行数据的序列化
SESSION_SERIALIZER = 'django.contrib.sessions.serializers.PickleSerializer'


MD5_SALT = "forever"


CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        #添加密码的第一种方式
        # "LOCATION": "redis://:123456@127.0.0.1:6379/1",
        "LOCATION": "redis://127.0.0.1:6379/1",
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
            #添加密码的第二种方式
            # "password":"123456"
        }
    }
}

#如下选项将session交给redis缓存来管理，减轻服务器的压力（指redis和服务器放在不同的机器上）
SESSION_ENGINE = "django.contrib.sessions.backends.cache" #将session交给redis缓存
SESSION_CACHE_ALIAS = "default"


#富文本框二配置上传文件（图片）路径
# MEDIA_URL = '/static/ueupload/'
# MEDIA_ROOT = './static/ueupload/'

MEDIA_URL = ''
MEDIA_ROOT = ''
#总页数
PAGE_SIZE = 2
