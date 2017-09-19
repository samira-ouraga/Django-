# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect
from time import gmtime, strftime

def index(request):
    return render(request, "sessions_words/index.html")


def adding(request):
    content = {}
    content["time"] = strftime("%Y-%m-%d %H:%M %p", gmtime()) 
    for key, value in request.POST.iteritems():
        if  key != "font":
            content[key] = value
        if key == "font":
            content['big'] = "big"
        else:
            content['big'] = ""   

    try:
        request.session['words']
    except KeyError:
        request.session['words'] = []

    new_dict = request.session["words"]
    new_dict.append(content) 
    request.session["words"] = new_dict
    for key, val in request.session.__dict__.iteritems():
        print key, val
    return redirect("/")



def clear(request):
    for key in request.session.keys():
        del request.session[key]
    return redirect("/")