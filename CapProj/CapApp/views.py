from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# from django.core.urlresolvers import reverse

from CapApp.models import Grant
from CapApp.stats import Stats

# Create your views here.

def index(request):
    if request.method == 'GET': # If the form is submitted
        search_query = request.GET.get('search_box', None)
        if search_query:
            return HttpResponseRedirect('grants')
    return render(request, 'CapApp/root.html')

def grants(request):
    #this is a way to save the query so it doesn't dissapear b/c of the pagination.
    #Probablly not the best way.
    query = request.GET.get('search_box', '')
    if query == "":
        query = request.session['query']
    else:
        request.session['query'] = query

    query = request.session['query']
    print(query)

    grant_list = Grant.objects.filter(abstract_text__search=query)
    paginator = Paginator(grant_list, 10)
    # Show 10 contacts per page
    page_number = request.GET.get('page')
    try:
        grants = paginator.page(page_number)
    except PageNotAnInteger:
        grants = paginator.page(1)
    except EmptyPage:
        grants = paginator.page(paginator.num_pages)

    grant_stats = Stats.return_stats_dict(grant_list, query)
    return render(request, 'CapApp/grants.html',{'grants': grants, 'grant_stats': grant_stats})



# def your_view(request):
#     ''' This could be your actual view or a new one '''
#     # Your code
#     if request.method == 'GET': # If the form is submitted
#
#         search_query = request.GET.get('search_box', None)

# def help(request):
#     helpdict = {'help_insert': 'HELP PAGE'}
#     return render(request, 'CapApp/help.html',context=helpdict)
