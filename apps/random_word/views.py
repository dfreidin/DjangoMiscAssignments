# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect
from django.utils.crypto import get_random_string

# Create your views here.
def index(request):
    if not "attempts" in request.session:
        request.session["attempts"] = 0
    request.session["attempts"] += 1
    word = get_random_string(length=14)
    context = {
        "word": word
    }
    return render(request, "random_word/index.html", context)