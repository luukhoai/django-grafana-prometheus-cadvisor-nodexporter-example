from django.conf.urls import url
from .views import MainIndexView


app_name = 'main'
urlpatterns = [
    url(r'^$', MainIndexView.as_view(), name='index'),
]