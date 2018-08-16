#- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.shortcuts import render, redirect, render_to_response
from django.views.decorators.csrf import csrf_exempt
from django.template import RequestContext
from django.contrib import auth
from django.contrib.auth.forms import UserCreationForm
from django import forms

@csrf_exempt
def index(request):
    if request.method == 'POST':
        print(request.POST['projectName'])
    context = RequestContext(request)
    context_dict = {'boldmessage': "I am a bold font from the context"}
    return render_to_response('TINKOFF/index.html', context_dict, context)

@csrf_exempt
def info(request):
    context = RequestContext(request)
    context_dict = {'boldmessage': "I am a bold font from the context"}
    return render_to_response('TINKOFF/info.html', context_dict, context)

@csrf_exempt
def reglaments(request):
    context = RequestContext(request)
    context_dict = {'boldmessage': "I am a bold font from the context"}
    return render_to_response('TINKOFF/reglaments.html', context_dict, context)

@csrf_exempt
def help(request):
    context = RequestContext(request)
    context_dict = {'boldmessage': "I am a bold font from the context"}
    return render_to_response('TINKOFF/help.html', context_dict, context)

@csrf_exempt
def support(request):
    context = RequestContext(request)
    context_dict = {'boldmessage': "I am a bold font from the context"}
    return render_to_response('TINKOFF/support.html', context_dict, context)

@csrf_exempt
def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = UserCreationForm()
    return render(request, 'TINKOFF/signup.html', {'form': form})
