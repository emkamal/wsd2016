from django.conf.urls import url

from . import views

# Note: the (?P<variablename>pattern) can be used to match a pattern and
# place the matched part of the string in the variable,
# in this case: blog_name

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<blog_name>[a-z0-9\-]+)$', views.blog, name='blog'),
]
