from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView

from department.forms import EquipmentCreateForm, EquipmentUpdateForm
from department.models import Sprzet


class EquipmentListView(ListView):
    template_name = 'department/equipment_list.html'
    model = Sprzet
    ordering = ('pk',)


class EquipmentCreateView(CreateView):
    template_name = 'department/equipment_form.html'
    model = Sprzet
    form_class = EquipmentCreateForm
    success_url = reverse_lazy('equipment-list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            "go_back": reverse('equipment-list')
        })
        return context


class EquipmentDetailView(DetailView):
    template_name = 'department/equipment_detail.html'
    model = Sprzet

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            "go_back": reverse('equipment-list')
        })
        return context


class EquipmentUpdateView(UpdateView):
    template_name = 'department/equipment_form.html'
    model = Sprzet
    form_class = EquipmentUpdateForm

    def get_success_url(self):
        return reverse('equipment-detail', args=(self.kwargs['pk'],))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            "go_back": reverse('equipment-detail', args=(self.kwargs['pk'],))
        })
        return context


class EquipmentDeleteView(DeleteView):
    model = Sprzet
    template_name = 'department/equipment_confirm_delete.html'
    success_url = reverse_lazy('equipment-list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            "go_back": reverse('equipment-detail', args=(self.kwargs['pk'],))
        })
        return context
