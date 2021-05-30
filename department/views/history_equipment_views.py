from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView

from department.forms import HistoryEquipmentCreateForm, HistoryEquipmentUpdateForm
from department.models import PrzegladSprzet


class HistoryEquipmentListView(ListView):
    template_name = 'department/history_equipment_list.html'
    model = PrzegladSprzet
    ordering = ('pk',)


class HistoryEquipmentCreateView(CreateView):
    template_name = 'department/history_equipment_form.html'
    model = PrzegladSprzet
    form_class = HistoryEquipmentCreateForm
    success_url = reverse_lazy('history-equipment-list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            "go_back": reverse('history-equipment-list')
        })
        return context


class HistoryEquipmentDetailView(DetailView):
    template_name = 'department/history_equipment_detail.html'
    model = PrzegladSprzet

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            "go_back": reverse('history-equipment-list')
        })
        return context


class HistoryEquipmentUpdateView(UpdateView):
    template_name = 'department/history_equipment_form.html'
    model = PrzegladSprzet
    form_class = HistoryEquipmentUpdateForm

    def get_success_url(self):
        return reverse('history-equipment-detail', args=(self.kwargs['pk'],))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            "go_back": reverse('history-equipment-detail', args=(self.kwargs['pk'],))
        })
        return context


class HistoryEquipmentDeleteView(DeleteView):
    model = PrzegladSprzet
    template_name = 'department/history_equipment_confirm_delete.html'
    success_url = reverse_lazy('history-equipment-list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            "go_back": reverse('history-equipment-detail', args=(self.kwargs['pk'],))
        })
        return context
