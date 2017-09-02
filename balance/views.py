# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from balance.models import *
from django.http import Http404

import logging
logging.basicConfig(filename='debug.log', level=logging.DEBUG)


def homepage(request):
    return render(request, 'homepage.html')


def profile_list(request):
    list_profile = User.objects.all()
    context = {
        'profile_list': profile_list
    }
    return render(request, 'profiles/profile_list.html', context)


def profile_detail(request, pk):
    try:
        user = User.objects.get(pk=pk)
    except User.DoesNotExist:
        raise Http404('User doesn\'t exist in the platform..')
    context = {
        'user': user
    }
    return render(request, 'profiles/profile_detail.html', context)
