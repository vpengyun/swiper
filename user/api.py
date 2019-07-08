from django.shortcuts import render


# Create your views here.
def verify_phone(request):
    """
    验证手机号
    :param request:
    :return:
    """
    phone_num = request.POST.get('phone_num','')
    phone_num = phone_num.strip()



    pass
def login(request):
    """
    用户登录
    :param request:
    :return:
    """
    pass
def get_profile(request):
    """
    获取用户信息
    :param request:
    :return:
    """
    pass

def set_profile(request):
    """
    设置用户信息
    :param request:
    :return:
    """
    pass

def upload_avatar(request):
    """
    更新用户信息
    :param request:
    :return:
    """
    pass


