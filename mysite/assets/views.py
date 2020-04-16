# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import models
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404

# Create your views here.
@csrf_exempt
def index(request):
    assets = models.Asset.objects.all()
    return render(request, 'index.html', locals())