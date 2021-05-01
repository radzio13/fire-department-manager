from django.views import View
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy, reverse
from department.models import Uslugi
from department.forms import ServiceCreateForm

class ServiceListView(ListView):
    template_name = 'department/service_list.html'
    model = Uslugi
    ordering = ('pk',)


class ServiceCreateView(CreateView):
    template_name = 'department/service_form.html'
    model = Uslugi
    form_class = ServiceCreateForm
    success_url = reverse_lazy('service-list')


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            "go_back": reverse('service-list')
        })
        return context


class ServiceDetailView(DetailView):
    template_name = 'department/service_detail.html'
    model = Uslugi

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            "go_back": reverse('service-list')
        })
        return context


class ServiceUpdateView(UpdateView):
    template_name = 'department/service_form.html'
    model = Uslugi
    form_class = ServiceCreateForm

    def get_success_url(self):
        return reverse('service-detail', args=(self.kwargs['pk'],))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            "go_back": reverse('service-detail', args=(self.kwargs['pk'],))
        })
        return context


class ServiceDeleteView(DeleteView):
    model = Uslugi
    template_name = 'department/service_confirm_delete.html'
    success_url = reverse_lazy('service-list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            "go_back": reverse('service-detail', args=(self.kwargs['pk'],))
        })
        return context
