# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse

# Create your views here.


def list_categories(request):

    return HttpResponse('Categories\' list here.')


def category(request, category_id):

    return HttpResponse("This is category {}. Category's posts here.".format(category_id))