from django.views.generic import TemplateView
from django.views.generic.base import TemplateResponseMixin, View
from .models import *

class HomeView(TemplateView):
    template_name = 'department/home.html'


class EquipmentView(TemplateView):
    template_name = 'department/equipment.html'
    
class VehicleView(TemplateResponseMixin, View):
    template_name = 'department/vehicle.html'

    def get(self, request):
        vehicles = Pojazdy.objects.all()
        return self.render_to_response({"vehicles": vehicles})