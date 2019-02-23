from django.shortcuts import render
from django.views.generic import TemplateView

from core.forms import SearchForm
from core.api import ItbookApi

def search(request):
    if request.method =='GET':
        return render(request, 'search.html')
    else:
        # validate submitted form
        form = SearchForm(request.POST)
        if form.is_valid():
            """query = form.cleaned_data['query']
            parameter = form.cleaned_data['parameter']"""
        results = ItbookApi().get_result()
        return render(request, 'result.html', {'results':results})