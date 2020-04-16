# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-10-29 08:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Asset',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('asset_type', models.CharField(choices=[('server', '\u670d\u52a1\u5668'), ('networkdevice', '\u7f51\u7edc\u8bbe\u5907'), ('storagedevice', '\u5b58\u50a8\u8bbe\u5907'), ('securitydevice', '\u5b89\u5168\u8bbe\u5907'), ('software', '\u8f6f\u4ef6\u8d44\u4ea7')], default='server', max_length=64, verbose_name='\u8d44\u4ea7\u7c7b\u578b')),
                ('name', models.CharField(max_length=64, unique=True, verbose_name='\u8d44\u4ea7\u540d\u79f0')),
                ('sn', models.CharField(max_length=128, unique=True, verbose_name='\u8d44\u4ea7\u5e8f\u5217\u53f7')),
                ('status', models.SmallIntegerField(choices=[(0, '\u5728\u7ebf'), (1, '\u4e0b\u7ebf'), (2, '\u672a\u77e5'), (3, '\u6545\u969c'), (4, '\u5907\u7528')], default=0, verbose_name='\u8bbe\u5907\u72b6\u6001')),
                ('c_time', models.DateTimeField(auto_now_add=True, verbose_name='\u6279\u51c6\u65e5\u671f')),
                ('m_time', models.DateTimeField(auto_now=True, verbose_name='\u66f4\u65b0\u65e5\u671f')),
            ],
            options={
                'ordering': ['c_time'],
                'verbose_name': '\u8d44\u4ea7\u603b\u8868',
                'verbose_name_plural': '\u8d44\u4ea7\u603b\u8868',
            },
        ),
    ]