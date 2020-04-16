# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from assets import models

class AssetAdmin(admin.ModelAdmin):
    list_display = ['asset_type', 'name', 'status', 'c_time', 'm_time']

admin.site.register(models.Asset, AssetAdmin)