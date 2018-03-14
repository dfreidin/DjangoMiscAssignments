# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect, HttpResponse

# Create your views here.
def index(request):
    return render(request, "amadon/index.html")

def checkout(request):
    return render(request, "amadon/checkout.html")

def buy(request):
    if not "count" in request.session:
        request.session["count"] = 0
    if not "total" in request.session:
        request.session["total"] = 0
    if request.method != "POST":
        return redirect(checkout)
    pid = int(request.POST["product_id"])
    quant = int(request.POST["quantity"])
    print "pid: {}".format(pid)
    print "quant: {}".format(quant)
    if quant < 0:
        return redirect(checkout)
    costs = {
        1: 19.99,
        2: 29.99,
        3: 4.99,
        4: 49.99
    }
    charge = costs.get(pid, 0) * quant
    print "charge: {}".format(charge)
    request.session["count"] += quant
    request.session["total"] += float(charge)
    request.session["charge"] = float(charge)
    return redirect(checkout)
    