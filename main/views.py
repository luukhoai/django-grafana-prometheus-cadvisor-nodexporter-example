from django.shortcuts import render
from django.views.generic.edit import CreateView
from test_django.views import BaseView
from products.models import Products
from snippets.models import Snippet
# Create your views here.


class MainIndexView(BaseView):
    template_name = 'main/index.html'

    def get_context_data(self, **kwargs):
        context = super(MainIndexView, self).get_context_data(**kwargs)
        context['products'] = Products.objects.all()
        context['snippets'] = Snippet.objects.all()
        return context



