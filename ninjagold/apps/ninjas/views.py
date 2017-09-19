# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect

def index(request):
    
    return render(request, "ninjas/index.html")


def process(request):
    try:
        request.session['activities']
    except KeyError:
        request.session['activities'] = []
    
    request.session["building"] = request.POST["building"]

    temp_list = request.session['activities']
    if request.session["building"] == "farm":
        temp_list.append("in the farm , you won 10 golds")

    elif request.session["building"] == "house":
        temp_list.append("in the house , you won 10 golds")
    
    elif request.session["building"] == "cave":
        temp_list.append("in the cave , you won 60 golds")

    elif request.session["building"] == "casino":
        temp_list.append("in the casino , you lost 40 golds")
    
    request.session['activities'] = temp_list

    try:
        request.session['total']
    except KeyError:
        request.session['total'] = 0
    if request.session["building"] == "farm":
        request.session["total"] += 10
    elif request.session["building"] == "house":
        request.session["total"] += 10
    elif request.session["building"] == "cave":
        request.session["total"] += 60
    elif request.session["building"] == "casino":
        request.session["total"] -= 40

    return redirect( "/")
    

def clear(request):
    for key in request.session.keys():
        del request.session[key]
    return redirect("/")