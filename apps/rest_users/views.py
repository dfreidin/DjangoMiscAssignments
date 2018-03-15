# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from .models import *

# Create your views here.

def index(request):
    all_users = []
    for user_data in User.objects.all():
        user = {}
        user["id"] = user_data.id
        user["name"] = "{} {}".format(user_data.first_name, user_data.last_name)
        user["email"] = user_data.email
        user["created"] = user_data.created_at.strftime("%c")
        all_users.append(user)
    return render(request, "rest_users/index.html", {"all_users": all_users})

def show(request, id):
    user = {}
    user_data = User.objects.get(id=id)
    user["id"] = user_data.id
    user["name"] = "{} {}".format(user_data.first_name, user_data.last_name)
    user["email"] = user_data.email
    user["created"] = user_data.created_at.strftime("%c")
    return render(request, "rest_users/show.html", {"user": user})

def new(request):
    form = UserForm()
    return render(request, "rest_users/new.html", {"form": form})

def edit(request, id):
    user = User.objects.get(id=id)
    data = {
        "first_name": user.first_name,
        "last_name": user.last_name,
        "email": user.email
    }
    form = UserForm(initial=data)
    return render(request, "rest_users/edit.html", {"form": form, "id": id})

def create(request):
    if request.method != "POST":
        return redirect(new)
    form = UserForm(request.POST)
    if form.is_valid():
        new_user = form.save()
        return redirect(show, id=new_user.id)
    return redirect(new)

def update(request, id):
    if request.method != "POST":
        return redirect(new)
    form = UserForm(request.POST, instance=User.objects.get(id=id))
    if form.is_valid():
        user = form.save()
        return redirect(show, id=user.id)
    return redirect(new)

def destroy(request, id):
    User.objects.get(id=id).delete()
    return redirect(index)