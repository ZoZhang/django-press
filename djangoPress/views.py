from django.shortcuts import render
from django.urls import reverse
from django.views.generic import TemplateView, ListView, DetailView, FormView

# All view.

class HomeIndex(TemplateView):
    template_name = 'home/index.html'

