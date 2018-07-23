from django.shortcuts import render
from django.views.generic.edit import FormView
from .forms import UserLoginForm
from django.contrib.auth import login, logout, get_user, get_user_model, authenticate
from django.http.response import JsonResponse
from django.views.generic.base import View
from django.core.exceptions import ValidationError
import logging

logger = logging.getLogger('test_django')


class UserLoginFormView(FormView):
    template_name = 'main/index.html'
    form_class = UserLoginForm

    def form_valid(self, form):
        username = self.request.POST['username']
        password = self.request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(self.request, user)
            return JsonResponse({'success': True})
        else:
            return JsonResponse({'success': False,
                                 'message': 'Username or Password in correct. Please try again'})

    def form_invalid(self, form):
        error_message = ''
        for f, e in form.errors.items():
            error_message += e.get_json_data()[0]['message'] + '<br>'
        return JsonResponse({'success': False, 'message': error_message})
