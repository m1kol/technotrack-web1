# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse

# Create your views here.


def list_posts(request):

    return HttpResponse("Posts' list should be here.")


def show_post(request, post_id):

    return HttpResponse("Post number {} should be shown.".format(post_id))