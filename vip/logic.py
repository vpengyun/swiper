def has_perm(perm_name):
    '''
    @has_perm('superlike')
    :param perm_name:
    :return:
    '''
    def decorator(view_func):
        def wapper(request,*args,**kwargs):
            pass
        return wapper
    return decorator
