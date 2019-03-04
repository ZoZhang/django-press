from djangoPress.model.category import Category
from django import template

register = template.Library()


@register.inclusion_tag('base/navigation.html')
def categorys(selected_id=None):
    data = Category.objects.all().filter(is_active=True)
    return {
        'categorys': data,
        'selected': selected_id,
    }

