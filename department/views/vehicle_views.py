from django.views import View
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy, reverse
from department.models import Pojazdy
from department.forms import VehicleCreateForm
from django.contrib.auth.mixins import PermissionRequiredMixin

class VehicleListView(ListView):
    template_name = 'department/vehicle_list.html'
    model = Pojazdy
    ordering = ('pk',)


class VehicleCreateView(PermissionRequiredMixin, CreateView) :
    template_name = 'department/vehicle_form.html'
    model = Pojazdy
    form_class = VehicleCreateForm
    success_url = reverse_lazy('vehicle-list')
    permission_required = 'department.can_add_pojazdy'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            "go_back": reverse('vehicle-list')
        })
        return context


class VehicleDetailView(DetailView):
    template_name = 'department/vehicle_detail.html'
    model = Pojazdy

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            "go_back": reverse('vehicle-list')
        })
        return context


class VehicleUpdateView(PermissionRequiredMixin, UpdateView):
    template_name = 'department/vehicle_form.html'
    model = Pojazdy
    form_class = VehicleCreateForm
    permission_required = 'department.can_change_pojazdy'


    def get_success_url(self):
        return reverse('vehicle-detail', args=(self.kwargs['pk'],))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            "go_back": reverse('vehicle-detail', args=(self.kwargs['pk'],))
        })
        return context


class VehicleDeleteView(PermissionRequiredMixin, DeleteView):
    model = Pojazdy
    template_name = 'department/vehicle_confirm_delete.html'
    success_url = reverse_lazy('vehicle-list')
    permission_required = 'department.can_delete_pojazdy'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            "go_back": reverse('vehicle-detail', args=(self.kwargs['pk'],))
        })
        return context
