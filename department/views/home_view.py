from django.views.generic import TemplateView
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView

from department.models import Pojazdy, Sprzet

class HomeListView(ListView):
    template_name = 'department/home.html'
    model = Pojazdy
    ordering = ('pk',)


class HomeListViewEquipment(ListView):
    template_name = 'department/home_equipment.html'
    model = Sprzet
    ordering = ('pk',)
