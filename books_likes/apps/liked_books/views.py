# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse,redirect
from .models import User, Book, Review

# Create your views here.
def index(request):
    context={
        "users" : User.objects.all(),
        "books" : Book.objects.all(),
        "reviews": Review.objects.all(),
    

    }
    return render(request, 'liked_books/index.html',context)

def user(request):
    context={
        "users" : User.objects.all()
    }
    return render (request, 'liked_books/user.html', context)


def book(request):
    context={
        "books" : Book.objects.all(),
    }
    return render (request, 'liked_books/book.html',context)