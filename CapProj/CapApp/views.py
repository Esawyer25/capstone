from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
# from django.core.urlresolvers import reverse

from CapApp.models import Grant

# Create your views here.

def index(request):
    if request.method == 'GET': # If the form is submitted
        search_query = request.GET.get('search_box', None)
        print(search_query)
        print(search_query)
        if search_query:
            return HttpResponseRedirect('grants')
    return render(request, 'CapApp/root.html')

def grants(request):
    query = request.GET.get('search_box', '')
    print(query)
    grant_list = Grant.objects.filter(abstract_text__search=query)
    print(grant_list)
    # grant_list = Grant.objects.order_by('application_id')
    grant_dict = {"grants":grant_list}
    return render(request, 'CapApp/grants.html',context=grant_dict)

# def your_view(request):
#     ''' This could be your actual view or a new one '''
#     # Your code
#     if request.method == 'GET': # If the form is submitted
#
#         search_query = request.GET.get('search_box', None)

# def help(request):
#     helpdict = {'help_insert': 'HELP PAGE'}
#     return render(request, 'CapApp/help.html',context=helpdict)
