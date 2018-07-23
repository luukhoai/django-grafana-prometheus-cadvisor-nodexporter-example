from django.views.generic.edit import CreateView
from .forms import MainForm


class BaseView(CreateView):
    template_name = 'main/index.html'
    form_class = MainForm

    def get_context_data(self, **kwargs):
        context = super(BaseView, self).get_context_data(**kwargs)
        return context
