from django.db import models
from django.core.urlresolvers import reverse


class Tag(models.Model):
    name = models.CharField(max_length=50, db_index=True, unique=True)
    slug = models.SlugField(max_length=50, db_index=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('tagged_posts', (self.slug, ))


class Post(models.Model):
    title = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    body = models.TextField()
    posted = models.DateTimeField(db_index=True, auto_now_add=True)
    tags = models.ManyToManyField(Tag, blank=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post_view', args=(str(self.slug), ))
