from django.urls import reverse
from django.views.generic import TemplateView, FormView

from djangoPress.form.search import FormSearch

# Page Home


class HomeIndex(TemplateView):
    template_name = 'home/index.html'


# Page Search


class HeaderSearch(FormView):
    form_class = FormSearch
    template_name = 'search/header.html'
