from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib import messages
from django.http import HttpResponseRedirect

from core.forms import SearchForm
from core.api import ItbookApi

def search_by_name(query):
    result = ItbookApi(query).get_result()
    books = filter(lambda x : x['title'] == query, result)
    return books

def search(request):
    if request.method =='GET':
        return render(request, 'search.html')
    else:
        form = SearchForm(request.POST)
        if form.is_valid():
            query = form.cleaned_data['query']
            parameter = form.cleaned_data['parameter']
            if parameter == 'all' and query is not None:
                results = ItbookApi(query).get_result()
                return render(request, 'result.html', {'query': query, 'results': results})
            elif parameter == 'name' and query is not None:
                results = search_by_name(query)
                return render(request, 'result.html', {'query': query, 'results': results})        
            else:
                messages.error(request, 'Invalid search entry.')
                return HttpResponseRedirect('/')
        else:
            messages.error(request, 'Invalid search entry.')
            return HttpResponseRedirect('/')

