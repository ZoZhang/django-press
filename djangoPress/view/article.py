from django.views.generic import DetailView

# Article View
from djangoPress.model.article import Article


class ArticleView(DetailView):
    model = Article
    template_name = 'article/view.html'

