from django.views.generic import TemplateView
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView

from department.models import Pojazdy, Sprzet, Uslugi, Strazacy

class HomeListView(ListView):
    template_name = 'department/home.html'
    queryset = Pojazdy.objects.all()
    
    def get_context_data(self, **kwargs):
    	context = super(HomeListView, self).get_context_data(**kwargs)
    	context['pojazdy'] = Pojazdy.objects.all()
    	context['uslugi'] = Uslugi.objects.all()
    	context['sprzet'] = Sprzet.objects.all()
    	context['strazacy'] = Strazacy.objects.all()
    	return context
    	
