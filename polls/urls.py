from django.conf.urls import patterns
from django.conf.urls import url


urlpatterns = patterns('polls.views',
    # Examples:
    url(r'^$', 'index', name='index'),

)