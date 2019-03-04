from django.views.generic import TemplateView

# Page Home


class HomeIndex(TemplateView):
    template_name = 'home/index.html'
