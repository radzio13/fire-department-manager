from django.views.generic import TemplateView

from department.models import UwagaSprzet, UwagaStrazacy, UwagaPojazdy, UwagaUslugi


class HomeView(TemplateView):
    template_name = 'department/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context.update({
            "firefighters": UwagaStrazacy.objects.order_by('created_at'),
            "equipments": UwagaSprzet.objects.order_by('created_at'),
            "vehicles": UwagaPojazdy.objects.order_by('created_at'),
            "services": UwagaUslugi.objects.order_by('created_at'),
        })
        return context
