from django.conf.urls import url
from . import views

          

urlpatterns= [
    url(r'^$', views.index, name='index'), #render index.html 
    url(r'^register$', views.register, name='register'), #redirect to views.index
    url(r'^login$', views.login, name='login'), #redirect to views.Index

    url(r'^books$', views.books, name="books"),  #render books.html , click to add review 
    url(r'^add', views.add, name="add"), #render add.html with book review form with action process
    url(r'^create$', views.create, name='create'), #redirect to views.books 


    url(r'^books/(?P<book_number>\d+)$', views.book, name="book"), #render book.html
    url(r'^users/(?P<user_number>\d+)$', views.user, name="user"), #render user.html 
    url(r'^logout$', views.logout, name="logout"), #delete session, redirect to index 
    url(r'^delete_review$', views.delete_review, name="delete_review"), #delete review 
      
]


