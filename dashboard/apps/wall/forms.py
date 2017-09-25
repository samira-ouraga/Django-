from django import forms 
import datetime

class RegistrationForm(forms.Form):
    first_name = forms.CharField(label='First name', max_length=100)
    last_name = forms.CharField(label='Last name', max_length=100)
    email = forms.CharField(label='Email', max_length=100)
    password = forms.CharField(label='Password', max_length=100)
    cpassword = forms.CharField(label='Confirm password', max_length=100)


class LoginForm(forms.Form):
    email = forms.CharField(label='Email', max_length=100)
    password = forms.CharField(label='Password', max_length=100)



class BookForm(forms.Form):
    book_title = forms.CharField(label='Book Title', max_length=100)
    author = forms.CharField(label='Author', max_length=30)
    review = forms.CharField(label='Review', max_length=255)
