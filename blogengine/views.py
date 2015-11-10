from django.views import generic
from blogengine import models


class PostsView(generic.ListView):
    def get_queryset(self):
        return models.Post.objects.order_by('-posted')[:5]


class PostDetail(generic.DetailView):
    model = models.Post