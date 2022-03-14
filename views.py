import os
from os import chdir

from django.http import HttpResponse
from django.shortcuts import render
import datetime


def index(request):
    return HttpResponse('hello from django')


def current_time(request):
    return HttpResponse(f'Time = {datetime.datetime.now()}')


def work(request):
    path = os.path.join(os.getcwd(),'views.py')
    return HttpResponse(f"workdir = {path}")
