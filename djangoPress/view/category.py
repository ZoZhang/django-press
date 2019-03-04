from django.views.generic import ListView

# Category List
from djangoPress.model.article import Article
from djangoPress.model.category import Category


class CategoryList(ListView):
    model = Category
    template_name = 'category/list.html'

    def get_context_data(self, **kwargs):
        context = super(CategoryList, self).get_context_data(**kwargs)
        context['current_category'] = self.get_category
        context['article_list'] = self.get_article
        return context

    def get_article(self):
        word = self.kwargs['word']
        try:
            data = Article.objects.filter(category__slug=word, status=2)
        except Category.DoesNotExist:
            data = None

        return data

    def get_category(self):
        word = self.kwargs['word']
        try:
            data = Category.objects.get(slug=word)
        except Category.DoesNotExist:
            data = None

        return data
