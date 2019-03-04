
from django import template

register = template.Library()

language_flags = [
    {'code': 'fr', 'label': 'France'},
    {'code': 'en', 'label': 'English'}
]


@register.inclusion_tag('base/flags.html', takes_context=True)
def flags_language(context):
    return {'flags': language_flags}
