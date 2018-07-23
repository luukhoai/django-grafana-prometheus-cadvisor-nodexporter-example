from django.conf.urls import url
from snippets.views import SnippetList, SnippetDetail, SnippetHighlight
from rest_framework.urlpatterns import format_suffix_patterns

app_name = 'snippets'
urlpatterns = [
    url(r'^$', SnippetList.as_view(), name='list'),
    url(r'^(?P<pk>[0-9]+)/$', SnippetDetail.as_view(), name='detail'),
    url(r'^(?P<pk>[0-9]+)/highlight/$', SnippetHighlight.as_view(), name='highlight')
]


