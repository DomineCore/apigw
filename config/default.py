import env

from django.conf import settings

INSTALLED_APPS = settings.INSTALLED_APPS + [
    # 网关路由转发
    'apischedule',
    # 网关请求记录
    'requestrec',
    # 应用认证
    'oauth.appauth',
    # api调试器
    'apidebuger',
    # 应用管理器
    'resource.appman',
    # apisentry 存储api调用traceback
    'resource.apisentry'
]

MIDDLEWARE = settings.MIDDLEWARE + [

]

DEFAULT_SYS_NAME = 'apigw'

# APIGW访问地址
APIGW_HOST = env.APIGW_HOST

# 网关URL
APIGW_ROOT_URL = APIGW_HOST.rstrip("/") + "/apigw/"
