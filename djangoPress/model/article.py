from django.db import models
from django.utils import timezone

from djangoPress.model.category import Category

DRAFT = 1
TRASHED = 3
PUBLISHED = 2

STATUS_ARTICLE = (
    (DRAFT, 'Draft'),
    (TRASHED, 'Trashed'),
    (PUBLISHED, 'Published')
)


class Article(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=150)
    slug = models.SlugField(max_length=255, unique=True)
    status = models.SmallIntegerField(choices=STATUS_ARTICLE)
    image = models.FileField(blank=True, null=True)
    short_description = models.TextField(max_length=140)
    body = models.TextField()
    meta_description = models.TextField(max_length=160, null=True, blank=True)
    meta_keywords = models.TextField(max_length=255, null=True, blank=True)
    created_date = models.DateTimeField(default=timezone.now)
    updated_date = models.DateTimeField(blank=True, null=True)
    published_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        ordering = ('-created_date',)

    def save(self, *args, **kwargs):
        self.updated_date = timezone.now()

        if PUBLISHED == self.status:
            self.published_date = timezone.now()
        else:
            self.published_date = None

        super(Article, self).save(*args, **kwargs)

    def __str__(self):
        return self.title

