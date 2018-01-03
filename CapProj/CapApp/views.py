from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse("hello world")

def help(request):
    helpdict = {'help_insert': 'HELP PAGE'}
    return render(request, 'CapApp/help.html',context=helpdict)
