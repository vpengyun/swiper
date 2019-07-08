from django.db import models


# Create your models here.
class Vip(models.Model):
    '''
    会员
    '''

    name = models.CharField(max_length=32, unique=True)
    level = models.IntegerField(default=0, unique=True)
    price = models.DecimalField(max_digits=5, decimal_places=2, default=0)

    @property
    def perms(self):
        '''
        vip 所对应的权限
        :return:
        '''
        if not hasattr(self, '_perms'):
            vip_perms = VipPermission.objects.filter(vip_id=self.id).only('perm_id')
            perm_id_list = [p.perm_id for p in vip_perms]
            perms = Permission.objects.filter(id_in=perm_id_list).only('name')
            self._perms = perms
        return self._perms

    def has_perm(self, perm_name):
        """
        检查当前vip等级是否拥有某种权限
        :param perm_name:
        :return:
        """

        perm_names = [p.name for p in self.perms]
        return perm_name in perm_names

    class Meta:
        db_table = 'vips'


class Permission(models.Model):
    '''
    权限
    '''
    name = models.CharField(max_length=32, unique=True)
    description = models.TextField()

    class Meta:
        db_table = 'permission'


class VipPermission(models.Model):
    '''
    vip-权限关系表
    '''
    vip_id = models.IntegerField()
    perm_id = models.IntegerField()

    class Meta:
        db_table = 'vip_permission'
