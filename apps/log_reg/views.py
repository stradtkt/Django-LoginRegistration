# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from .models import *
# Create your views here.
def index(request):
    return render(request, 'log_reg/index.html')

def login_page(request):
    return render(request, 'log_reg/login.html')

def register_page(request):
    return render(request, 'log_reg/register.html')

def register(request):
    first_name = request.POST['first_name']
    last_name = request.POST['last_name']
    email = request.POST['email']
    password = request.POST['password']
    errors = User.objects.validate(first_name, last_name, email, password)
    if len(errors) == 0:
        User.objects.create(first_name=first_name, last_name=last_name, email=email, password=password)
        return HttpResponse("Added to the database")
    else:
        for message in errors:
            messages.error(request, message)
    return redirect('/')

def login(request):
    email = request.POST['email']
    password = request.POST['password']
    result = User.objects.validateLogin(email, password)
    if result[0]:
        request.session["id"] = result[1]
        return redirect("/")
    else:
        for message in result[1]:
            messages.error(request, message)
        return redirect("/")
