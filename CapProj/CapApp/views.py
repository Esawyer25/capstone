from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# import pubmed_parser as pp
import requests
import datetime
import time
from django.core.exceptions import ValidationError

# from django.core.urlresolvers import reverse
from CapApp.pubmed import Pubmed
from CapApp.models import Grant, Keyword
from CapApp.custom_classes import Stats, Add_Keyword

# Create your views here.

def index(request):
    # request.session['query'] = None
    top_ten_searches = Keyword.objects.all()
    if top_ten_searches.count() > 10:
        top_ten_searches = top_ten_searches[0:10]

    #none of this is working b/c the search form submits to grants b/c the urls are messed up
    errors = []
    if 'q' in request.GET:
        q = request.GET['q']
        if not q:
            print('if not q')
            errors.append('Enter a search term.')
        elif len(q) > 30:
            errors.append('Please enter at most 30 characters.')
        else:
            print(q==None)
            return HttpResponseRedirect('grants')

    return render(request, 'CapApp/root.html', {'top_ten_searches': top_ten_searches, 'errors': errors})



def grants(request):
    #this is a way to save the query so it doesn't dissapear b/c of the pagination.
    #Probablly not the best way.
    query = request.GET.get('q', '')
    if query == "":
        query = request.session['query']
    else:
        request.session['query'] = query

    query = request.session['query']
    print(f'this is the query {query}')

    # if not query:
    #     top_ten_searches = Keyword.objects.all()
    #     if top_ten_searches.count() > 10:
    #         top_ten_searches = top_ten_searches[0:10]
    #     errors = ['enter a search term']
    #     return render(request, 'CapApp/root.html', {'top_ten_searches': top_ten_searches, 'errors': errors})


    try:
        keyword_object = Keyword.objects.get(keyword__iexact=query)
    except:
        keyword_object = None

    print(f'this is the keyword_object {keyword_object}')

    a = datetime.datetime.now()
    if keyword_object:
        keyword_object.searches += 1
        print(keyword_object.searches)

        try:
            Keyword.full_clean(keyword_object)
        except ValidationError as e:
            print(e)
        try:
            keyword_object.save()
        except:
            print(f"there was a problem saving with Keyword {query}")


        grant_list_long = keyword_object.grants.all()
        if grant_list_long.count() > 100:
            grant_list_short = grant_list_long[0:100]
        else:
            grant_list_short = grant_list_long
        b = datetime.datetime.now()
        print(f'time in database call for keyword = {b-a}')

    else:
        grant_list_long = Grant.objects.filter(project_terms__search=query)
        Add_Keyword.create_keyword(query, grant_list_long, searches=1)
        if grant_list_long.count() > 100:
            grant_list_short = grant_list_long[0:100]
        else:
            grant_list_short = grant_list_long
        b = datetime.datetime.now()
        print(f'time in database query for grants= {b-a}')

    c = datetime.datetime.now()
    paginator = Paginator(grant_list_short, 10)
    # Show 10 contacts per page
    page_number = request.GET.get('page')
    try:
        grants = paginator.page(page_number)
    except PageNotAnInteger:
        grants = paginator.page(1)
    except EmptyPage:
        grants = paginator.page(paginator.num_pages)

    d = datetime.datetime.now()
    print(f'time in pagination = {d-c}')

    e = datetime.datetime.now()
    grant_stats = Stats.return_stats_dict(grant_list_long, query)
    # grant_dict_stats= {'grant_stats': grant_stats}
    f = datetime.datetime.now()
    print(f'time for stats = {f-e}')

    print(f'total time: {datetime.datetime.now()-a}')
    # return render(request, 'CapApp/grants.html', grant_dict)

    # wordcloud = ["wordcloud1","wordcloud2","wordcloud3","wordcloud4","wordcloud5","wordcloud6","wordcloud7","wordcloud8","wordcloud9","wordcloud10" ]

    return render(request, 'CapApp/grants.html',{'grants':grants, 'grant_stats': grant_stats})

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
        temp = (Pubmed.parse_xml_web(paper.pmid, sleep=0.5, save_xml=False))
        all_papers.append(temp)
        # all_papers.append(Pubmed.parse_xml_web(paper.pmid, sleep=2, save_xml=False))
        index += 1
        # time.sleep(0.5)
    return render(request, 'CapApp/publications.html', {'all_papers':all_papers, 'focal': focal})


# def your_view(request):
#     ''' This could be your actual view or a new one '''
#     # Your code
#     if request.method == 'GET': # If the form is submitted
#
#         search_query = request.GET.get('search_box', None)

# def help(request):
#     helpdict = {'help_insert': 'HELP PAGE'}
#     return render(request, 'CapApp/help.html',context=helpdict)
