from django.views.generic import TemplateView
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView

from department.models import Pojazdy, Sprzet, UwagaSprzet, UwagaStrazacy, UwagaPojazdy, UwagaUslugi


class HomeListView(ListView):
    template_name = 'department/home.html'
    model = Pojazdy
    ordering = ('pk',)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context.update({
            "firefighters": UwagaStrazacy.objects.order_by('created_at'),
            "equipments": UwagaSprzet.objects.order_by('created_at'),
            "vehicles": UwagaPojazdy.objects.order_by('created_at'),
            "services": UwagaUslugi.objects.order_by('created_at'),
        })
        return context


class HomeListViewEquipment(ListView):
    template_name = 'department/home_equipment.html'
    model = Sprzet
    ordering = ('pk',)
