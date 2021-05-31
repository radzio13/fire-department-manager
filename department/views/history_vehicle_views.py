from django.views import View
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy, reverse
from department.models import PrzegladPojazdy
from department.forms import HistoryVehicleCreateForm
from django.contrib.auth.mixins import PermissionRequiredMixin

class HistoryVehicleListView(ListView):
    template_name = 'department/history_vehicle_list.html'
    model = PrzegladPojazdy
    ordering = ('pk',)


class HistoryVehicleCreateView(PermissionRequiredMixin, CreateView):
    template_name = 'department/history_vehicle_form.html'
    model = PrzegladPojazdy
    form_class = HistoryVehicleCreateForm
    success_url = reverse_lazy('history-vehicle-list')
    permission_required = 'department.can_add_przeglad_pojazdy'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            "go_back": reverse('history-vehicle-list')
        })
        return context


class HistoryVehicleDetailView(DetailView):
    template_name = 'department/history_vehicle_detail.html'
    model = PrzegladPojazdy

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            "go_back": reverse('history-vehicle-list')
        })
        return context


class HistoryVehicleUpdateView(PermissionRequiredMixin, UpdateView):
    template_name = 'department/history_vehicle_form.html'
    model = PrzegladPojazdy
    form_class = HistoryVehicleCreateForm
    permission_required = 'department.can_change_przeglad_pojazdy'

    def get_success_url(self):
        return reverse('history-vehicle-detail', args=(self.kwargs['pk'],))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            "go_back": reverse('history-vehicle-detail', args=(self.kwargs['pk'],))
        })
        return context


class HistoryVehicleDeleteView(PermissionRequiredMixin, DeleteView):
    model = PrzegladPojazdy
    template_name = 'department/history_vehicle_confirm_delete.html'
    success_url = reverse_lazy('vehicle-list')
    permission_required = 'department.can_delete_przeglad_pojazdy'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            "go_back": reverse('history-vehicle-detail', args=(self.kwargs['pk'],))
        })
        return context
