from django.urls import reverse_lazy
from department.forms import FirefighterCreateForm
from django.views.generic import ListView, CreateView
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from department.models import Strazacy
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.views.generic.base import View
from django.shortcuts import redirect

class RegisterUser(CreateView):
    template_name = 'registration/register.html'
    form_class = FirefighterCreateForm
    model = Strazacy
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        first_name = form.cleaned_data.get('first_name')
        last_name = form.cleaned_data.get('last_name')
        username = form.cleaned_data.get('username')
        email = form.cleaned_data.get('email')
        password = form.cleaned_data.get('password')
        user = User.objects.create_user(username, email, password, first_name=first_name, last_name=last_name, is_active=False)
        instance = form.save(commit=False)
        instance.user = user
        group = Group.objects.get(name='Członek')
        group.user_set.add(user)
        instance.save()
        return super().form_valid(form)


class InactiveUsersListView(PermissionRequiredMixin, ListView):
    template_name = 'department/inactive_users.html'
    model = Strazacy
    queryset = Strazacy.objects.filter(user__is_active = False)
    permission_required = 'department.can_add_strazacy'


class MakeActiveUser(PermissionRequiredMixin, View):
    permission_required = 'department.can_add_strazacy'
    
    def get(self, request, pk):
        user = User.objects.get(pk=pk)
        user.is_active = True
        user.save()
        return redirect(reverse_lazy('inactive-users'))