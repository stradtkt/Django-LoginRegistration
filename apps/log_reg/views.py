# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
import bcrypt
from .models import *
# Create your views here.
def index(request):
    return render(request, 'log_reg/index.html')

def login_page(request):
    return render(request, 'log_reg/login.html')

def register_page(request):
    return render(request, 'log_reg/register.html')

def dashboard(request):
    context = {"user": User.objects.get(id=request.session['id'])}
    return render(request, 'log_reg/dashboard.html', context)

def register(request):
    first_name = request.POST['first_name']
    last_name = request.POST['last_name']
    email = request.POST['email']
    password = request.POST['password']
    hashed_pw = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
    user = User.objects.create(first_name=first_name, last_name=last_name, email=email, password=hashed_pw)
    return redirect('/login-page')

def login(request):
    email = request.POST['email']
    password = request.POST['password']
    user = User.objects.filter(email=email)
    if len(user) > 0:
        is_pass = bcrypt.checkpw(password.encode(), user[0].password.encode())
        if is_pass:
            request.session['id'] = user[0].id
            messages.success(request, 'Successfully Logged In')
            return redirect('/dashboard')
        else:
            messages.error(request, "Incorrect items to login")
            return redirect('/')
    else:
        messages.error(request, "User does not exists")
        return redirect('/')
