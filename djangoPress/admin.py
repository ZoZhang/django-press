from django.contrib import admin

from djangoPress.models import Category

admin.site.register(Category)


admin.site.site_header = 'Django Press Administration'

