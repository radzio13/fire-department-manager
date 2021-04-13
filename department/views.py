from django.views.generic import TemplateView


class HomeView(TemplateView):
    template_name = 'department/home.html'


class EquipmentView(TemplateView):
    template_name = 'department/equipment.html'
