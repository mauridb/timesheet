# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from tablib import Dataset

from balance.models import *
from django.http import Http404, HttpResponse
from resources import TimesheetResource


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


def export(request):
    model_resource = TimesheetResource()
    dataset = model_resource.export()
    response = HttpResponse(dataset.csv, content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename={}.csv'.format('timesheet')
    return response


def simple_import(request):
    if request.method == 'POST':
        model_resource = TimesheetResource()
        dataset = Dataset()
        new_persons = request.FILES['myfile']

        imported_data = dataset.load(new_persons.read())
        result = model_resource.import_data(dataset, dry_run=True)  # Test the data import

        if not result.has_errors():
            model_resource.import_data(dataset, dry_run=False)  # Actually import now

    return render(request, 'coreapp/import.html')
