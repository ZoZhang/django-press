from djangoPress.model.article import Article
from django import template

register = template.Library()


@register.inclusion_tag('article/news.html')
def news():
    data = Article.objects.all().filter(status=2).order_by('-updated_date')
    return {
        'news': data,
    }

