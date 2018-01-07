from django.shortcuts import render
from django.http import HttpResponse
from CapApp.models import Grant

# Create your views here.

def index(request):
    # return HttpResponse("hello world")
    grant_list = Grant.objects.order_by('application_id')
    grant_dict = {"grants":grant_list}
    return render(request, 'CapApp/root.html',context=grant_dict)

# def help(request):
#     helpdict = {'help_insert': 'HELP PAGE'}
#     return render(request, 'CapApp/help.html',context=helpdict)
