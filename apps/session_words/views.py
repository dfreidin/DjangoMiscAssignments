# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from time import localtime, strftime

# Create your views here.
def index(request):
    return render(request, "session_words/index.html")

def add_word(request):
    if request.method == "POST":
        if not "words" in request.session:
            request.session["words"] = []
        if "size" in request.POST:
            s = request.POST["size"]
        else:
            s = "small"
        form_data = {
            "word": request.POST["word"],
            "color": request.POST["color"],
            "size": s,
            "time": strftime("%c", localtime())
        }
        request.session["words"].append(form_data)
        request.session.modified = True
    return redirect(index)

def clear(request):
    request.session["words"] = []
    return redirect(index)