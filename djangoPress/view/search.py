from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.views.generic import FormView

# Page Search
from djangoPress.model.article import Article


class Search(FormView):
    def start(request):
        query_str = str(request.GET.get('q'))

        if 'None' == query_str:
            return HttpResponseRedirect("/")
        else:
            data = Article.objects.all().filter(title__icontains=query_str, body__icontains=query_str, meta_keywords__icontains=query_str).distinct()

            return render_to_response('search/result.html', {'result': data, 'query': query_str})
