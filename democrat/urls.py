from django.conf.urls import patterns, include, url

from django.contrib import admin
from django.conf.urls.static import static

from democrat import settings

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', include('polls.urls')),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
)

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
# urlpatterns += patterns('',
#                         url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {
#                             'document_root': settings.STATIC_ROOT
#                         }),
#
# )