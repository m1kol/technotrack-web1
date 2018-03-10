# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse

# Create your views here.


def promt_login(request):

    return HttpResponse("This is login page. Login promt should be here.")