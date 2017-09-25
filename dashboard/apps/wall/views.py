# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from .forms import RegistrationForm, LoginForm, BookForm
from . import models 
from .models import User, UserManager, Book, User, Author, Review


# Create your views here.

def get_current_user(request):
    if 'current_user_id' in request.session:
        current_user = User.objects.get(id=request.session['current_user_id'])
        return current_user

def index(request):
    form1 = RegistrationForm()
    form2 = LoginForm()
    return render(request, 'wall/index.html', {'form1': form1, 'form2':form2})

def books(request):
    current_user = get_current_user(request)
    context={
        'users' : User.objects.all(),
        'current_user': current_user,
        'books': Book.objects.all(),
        'reviews': Review.objects.all(),
        'authors':Author.objects.all(),
    }
    return render(request, 'wall/books.html', context)

def logout(request):
    request.session.clear()
    return redirect('/')



def add(request):
    current_user = get_current_user(request)
    print current_user.first_name
    context = {
        'current_user': current_user,
        'form3':BookForm()

    }
    return render(request, 'wall/add.html', context)

def create(request):
    current_user = get_current_user(request)
    author_name =request.POST['author']
    author = Author.objects.filter(first_name=author_name)
    if len(author)<=0:
        author = Author.objects.create(
            first_name= request.POST['author']
        )
    
    newbook = Book.objects.create(
        title = request.POST['book_title']
    )
    Review.objects.create(
        user= current_user,
        notes= request.POST['review'],
        book= newbook
        )
    return redirect('/books/{}'.format( newbook.id))


def book(request,book_number):
    current_user = get_current_user(request)
    print current_user.first_name
    context={
        'book_number': book_number,
        'current_user': current_user,
        'current_book':Book.objects.filter(id=book_number),
        'reviews': Review.objects.filter(book__title='current_book')

    }
    print Review.objects.filter(book__title='current_book')
    

    return render(request, 'wall/book.html', context)


def register(request):
    if request.method == 'POST':
        current_user = User.objects.val_form(request)
        if current_user:
            request.session['current_user_id']= current_user.id
            return redirect('/books')
    return redirect("/")


def login(request):
    if request.method == 'POST':
        current_user = User.objects.val_login(request)
        if current_user:
            request.session['current_user_id']= current_user.id
            return redirect('/books')
    return redirect('/')



def user(request,user_number):
    current_user = get_current_user(request)
    return render(request, 'wall/user.html', user_number)


def delete_review(request, review_number):
    current_user = get_current_user(request)
    return redirect('/book', review_number)

