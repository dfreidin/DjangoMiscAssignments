# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from os.path import join

# Create your views here.
def index(request):
    return render(request, "file_upload/index.html")

def result(request):
    return render(request, "file_upload/result.html")

def process(request):
    if request.method != "POST":
        return redirect(index)
    if not "file" in request.FILES:
        request.session["file_message"] = "No file specified"
        request.session["file_category"] = "error"
        return redirect(result)
    f = request.FILES["file"]
    file_path = join("uploads", f.name)
    with open(file_path, "wb+") as destination:
        for chunk in f.chunks():
            destination.write(chunk)
        destination.close()
    request.session["file_message"] = "Success"
    request.session["file_category"] = "good"
    return redirect(result)