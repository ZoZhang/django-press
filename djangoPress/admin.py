from django.contrib import admin


from djangoPress.model.article import Article
from djangoPress.model.category import Category

admin.site.register(Category)
admin.site.register(Article)


admin.site.site_header = 'Django Press Administration'
