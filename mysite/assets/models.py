# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

# Create your models here.
class Asset(models.Model):
    asset_type_choice =(
        ('server', '服务器'),
        ('networkdevice', '网络设备'),
        ('storagedevice', '存储设备'),
        ('securitydevice', '安全设备'),
        ('software', '软件资产'),
    )
    asset_status = (
        (0, '在线'),
        (1, '下线'),
        (2, '未知'),
        (3, '故障'),
        (4, '备用'),
    )
    asset_type = models.CharField(choices=asset_type_choice, max_length=64, default='server', verbose_name="资产类型")
    name = models.CharField(max_length=64, unique=True, verbose_name="资产名称")  # 不可重复
    sn = models.CharField(max_length=128, unique=True, verbose_name="资产序列号")  # 不可重复
    status = models.SmallIntegerField(choices=asset_status, default=0, verbose_name='设备状态')

    c_time = models.DateTimeField(auto_now_add=True, verbose_name='批准日期')
    m_time = models.DateTimeField(auto_now=True, verbose_name='更新日期')
    def __str__(self):
        return '<%s>  %s' % (self.get_asset_type_display(), self.name)

    class Meta:
        verbose_name = '资产总表'
        verbose_name_plural = "资产总表"
        ordering = ['c_time']