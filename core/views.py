from django.shortcuts import render
from django.core.paginator import Paginator,EmptyPage, PageNotAnInteger
from django.contrib import messages
from django.http import HttpResponseRedirect

from core.forms import SearchForm, AddBookmarkForm
from core.api import ItbookApi
from core.models import Bookmark

#Sadece title'a göre ayrıca arama eklendi.
def search_by_name(query):
    result = ItbookApi(query).get_result()
    books = filter(lambda x : x['title'] == query, result)
    return books

def get_bookmark():
    results = []
    books = Bookmark.objects.all()
    return books

def search(request):
    if request.method =='GET':
        return render(request, 'search.html')
    else:
        form = SearchForm(request.POST)
        if form.is_valid():
            query = form.cleaned_data['query']
            parameter = form.cleaned_data['parameter']
            if parameter == 'Tümü' and query is not None:
                results = ItbookApi(query).get_result()
                return render(request, 'result.html', {'query': query, 'results': results})
            elif parameter == 'İsim' and query is not None:
                results = search_by_name(query)
                return render(request, 'result.html', {'query': query, 'results': results})        
            else:
                messages.error(request, 'Invalid search entry.')
                return HttpResponseRedirect('/')
        else:
            messages.error(request, 'Invalid search entry.')
            return HttpResponseRedirect('/') 

def addbookmark(request):
    form = AddBookmarkForm(request.POST)
    if form.is_valid():
        title = form.cleaned_data['title']
        title = form.save()    
    results = get_bookmark()
    return render(request, 'bookmark.html', {'results':results})     

