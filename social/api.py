from django.shortcuts import render

# Create your views here.
from libs.http import render_json
from social import logic
from social.models import Friend, Swiped
from social.permissions import has_perm
from user.models import User


def recommend(request):
    '''
    根据登录用户的profile筛选符合条件的用户
    :param request:
    :return:
    '''
    recm_users = logic.recommend_users(request.user)
    users = [u.to_dict() for u in recm_users]
    return render_json(data=users)


def like(request):
    '''
    喜欢
    :param request:
    :return:
    '''
    sid = int(request.POST.get('sid'))
    user = request.user

    matched = logic.like_someone(user.id, sid)

    return render_json(data={'matched': matched})


@has_perm('superlike')
def superlike(request):
    '''
    超级喜欢
    :param request:
    :return:
    '''
    sid = int(request.POST.get('sid'))
    user = request.user

    matched = logic.superlike_someone(user.id, sid)

    return render_json(data={'matched': matched})


def dislike(request):
    '''
    不喜欢
    :param request:
    :return:
    '''
    sid = int(request.POST.get('sid'))
    user = request.user

    ret = Swiped.swipe(uid=user.id, sid=sid, mark='dislike')

    # 只有滑动成功后，才可以进行增加积分操作
    if ret:
        logic.add_swipe_score('dislike', sid)

    return render_json()

@has_perm('rewind')
def rewind(request):
    '''
    反悔
    :param request:
    :return:
    '''
    user = request.user
    logic.rewind(user)

    return render_json()

@has_perm('liked_me')
def liked_me(request):
    '''
    喜欢我的人列表
    :param request:
    :return:
    '''
    liked_me_uid_list = logic.liked_me(request.user)

    users = User.objects.filter(id__in=liked_me_uid_list)

    user_list = [u.to_dict() for u in users]

    return render_json(data=user_list)


def friends(request):
    '''
    好友列表
    :param request:
    :return:
    '''
    friend_id_list = Friend.friend_list(request.user.id)

    my_friends = User.objects.filter(id__in=friend_id_list)
    friend_list = [u.to_dict() for u in my_friends]

    return render_json(data=friend_list)


def top10(request):
    '''
    人气排行榜
    :param request:
    :return:
    '''
    ret_data = logic.get_top_rank(10)

    rank_data = []

    for user, score in ret_data:
        user_dict = user.to_dict()
        user_dict['score'] = score
        rank_data.append(user_dict)

    return render_json(data=rank_data)
