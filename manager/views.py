from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
from django.utils.translation import gettext as _
from django.views.generic import ListView, FormView, TemplateView, DetailView


# Create your views here.
class IndexView(TemplateView):
    template_name = 'manager/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['logo'] = _("Task Manager")
        context['title'] = _("Task Manager")
        return context
