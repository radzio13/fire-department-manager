from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.views.generic.base import TemplateResponseMixin, View

class HomePage(TemplateResponseMixin, View):
    template_name = 'department/home.html'

    def get(self, request):
        return self.render_to_response({})