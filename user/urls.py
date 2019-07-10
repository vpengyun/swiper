from django.urls import path

from user import api

urlpatterns = [
    path('verify-phone', api.verify_phone),    # 手机号验证，并发送验证码
    path('login', api.login),                  # 验证码登录
    path('get-profile', api.get_profile),      # 获取用户信息
    path('set-profile', api.set_profile),      # 设置用户信息,form验证
    path('upload-avatar', api.upload_avatar),  # 更新用户头像本地保存并上传云存储
]
