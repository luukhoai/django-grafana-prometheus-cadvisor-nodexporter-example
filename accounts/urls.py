from django.conf.urls import url
from .views import UserLoginFormView
from main.views import MainIndexView

app_name = 'accounts'
urlpatterns = [
    url(r'^$', MainIndexView.as_view(), name='index'),
    url(r'^login$', UserLoginFormView.as_view(), name='login'),
]