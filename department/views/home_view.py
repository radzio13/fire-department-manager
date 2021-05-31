from django.views.generic import TemplateView

from department.models import (
    Uslugi, Strazacy, Pojazdy, Sprzet, UwagaSprzet, UwagaStrazacy, UwagaPojazdy, UwagaUslugi,
    UwagaPrzegladSprzet, UwagaPrzegladPojazdy
)


class HomeListView(TemplateView):
    template_name = 'department/home.html'

    def get_context_data(self, **kwargs):
        context = super(HomeListView, self).get_context_data(**kwargs)
        context['pojazdy'] = Pojazdy.objects.all()
        context['uslugi'] = Uslugi.objects.all()
        context['sprzet'] = Sprzet.objects.all()
        context['strazacy'] = Strazacy.objects.all()
        uwagi = list(UwagaStrazacy.objects.order_by('created_at')) \
                + list(UwagaSprzet.objects.order_by('created_at')) \
                + list(UwagaPojazdy.objects.order_by('created_at')) \
                + list(UwagaUslugi.objects.order_by('created_at')) \
                + list(UwagaPrzegladPojazdy.objects.order_by('created_at')) \
                + list(UwagaPrzegladSprzet.objects.order_by('created_at'))
        context.update({
            "uwagi": uwagi,
        })
        return context
