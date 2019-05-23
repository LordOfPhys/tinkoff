#- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.shortcuts import render, redirect, render_to_response
from django.views.decorators.csrf import csrf_exempt
from django.template import RequestContext
from django.contrib import auth
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from TINKOFF.models import UserProfile, UserTask
from django.core.mail import send_mail

@csrf_exempt
def index(request):
    context = RequestContext(request)
    context_dict = {'boldmessage': "I am a bold font from the context"}
    if request.user is not None and request.user.is_active:
        context_dict = {'task': UserTask.objects.get(user = request.user).take_task(), 'time': UserTask.objects.get(user = request.user).take_date()}
    if request.method == 'POST':
        user = request.user
        if user is not None and request.user.is_active:
            UserTask.objects.get(user = request.user).make_task(request.POST['task'])
            UserTask.objects.get(user = request.user).make_date(request.POST['date'])
        else:
            return redirect('../login')
    return render_to_response('TINKOFF/index.html', context_dict, context) #need to redirect to new page

@csrf_exempt
def log(request):
    context = RequestContext(request)
    if request.method == 'POST':
        a = request.POST['login']
        b = request.POST['password']
        user = authenticate(username=a, password=b)
        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect('../index')
            else:
                context_dict = {'boldmessage': "Данный аккаунт неактивен"}
                return render_to_response('TINKOFF/login.html', context_dict, context)
        else:
            context_dict = {'boldmessage': "Неверный логин или пароль"}
            return render_to_response('TINKOFF/login.html', context_dict, context)
    context_dict = {'boldmessage': ""}
    return render_to_response('TINKOFF/login.html', context_dict, context)

@csrf_exempt
def logout_view(request):
    auth.logout(request)
    return render(request,'TINKOFF/index.html')
