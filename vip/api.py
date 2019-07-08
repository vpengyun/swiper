from django.shortcuts import render

# Create your views here.
from vip.models import Vip


def vip_info(request):
    """
    vip 信息
    :param request:
    :return:
    """
    vip_info = []
    for vip in Vip.objects.all().order_by('level'):
        v_info = vip.to_dict()
        v_info['perms']=[]
        for perm in vip.perms:
            v_info['perms'].append(perm.to_dict())


    result = {
        'vip_level': request.vip.level,
        'vip_info': vip_info
    }
    return render_json(data=result)