from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# import pubmed_parser as pp
import requests
import time

# from django.core.urlresolvers import reverse
from CapApp.pubmed import Pubmed
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


#https://github.com/titipata/pubmed_parser
#if you use this package please cite: Titipat Achakulvisut, Daniel E. Acuna (2015) "Pubmed Parser" http://github.com/titipata/pubmed_parser. http://doi.org/10.5281/zenodo.159504
def publications(request):
    app_id = request.GET.get('app_id', '')
    #why do I sometimes get many more than one result for the same core project number when I only have 2018 loaded? this is happening for P60AA009803, P01HL018646, but not RO1s?  Switched to app_id to avoid problem.
    focal = Grant.objects.get(application_id = app_id)
    list_papers = focal.list_of_papers()
    print(list_papers)
    all_papers = []
    index = 1
    for paper in list_papers:
        temp = (Pubmed.parse_xml_web(paper.pmid, sleep=2, save_xml=False))
        all_papers.append(temp)
        # all_papers.append(Pubmed.parse_xml_web(paper.pmid, sleep=2, save_xml=False))
        index += 1
        # time.sleep(0.5)
    return render(request, 'CapApp/publications.html', {'all_papers':all_papers, 'focal': focal})




    # url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&id=" + "25845707" +"&retmode=text&rettype=abstract"
    # print(url)
    # r = requests.get(url)
    # call = requests.get(url)
    # print(call)
    # data = pp.parse_pubmed_xml(call)
    # print(data)
    # json = r.json()
    # print(call.json())
    # serializer = EmbedSerializer(data=json)


# def your_view(request):
#     ''' This could be your actual view or a new one '''
#     # Your code
#     if request.method == 'GET': # If the form is submitted
#
#         search_query = request.GET.get('search_box', None)

# def help(request):
#     helpdict = {'help_insert': 'HELP PAGE'}
#     return render(request, 'CapApp/help.html',context=helpdict)
