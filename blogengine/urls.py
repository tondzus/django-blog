from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^post/(?P<slug>[a-zA-Z0-9\-]+)/$', views.PostDetail.as_view(), name='post_view'),
    url(r'^$', views.PostsView.as_view(), name='index'),
]
