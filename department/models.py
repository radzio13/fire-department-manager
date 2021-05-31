from enum import auto, Enum

from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.db import models
from datetime import date, timedelta

from django.urls import resolve, reverse


class Sprzet(models.Model):
    nazwa = models.CharField(max_length=300)
    marka = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    parametry = models.TextField(blank=True)
    rok_prod = models.PositiveIntegerField()
    status = models.CharField(max_length=50)
    stan = models.CharField(max_length=50)
    uwagi = models.TextField(blank=True)

    def __str__(self):
        return f"{self.nazwa}, {self.marka} ({self.model})"


class Strazacy(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    data_urodzenia = models.DateField()
    data_wstapienia = models.DateField()
    ostatnie_badanie = models.DateField()
    nastepne_badanie = models.DateField()
    ubezpieczenie = models.DateField()
    kierowca = models.BooleanField(default=False,blank=True)
    termin_prawa_jazdy = models.DateField(blank=True, null=True)
    termin_wkladki = models.DateField(blank=True, null=True)
    termin_kpp = models.DateField(blank=True, null=True)
    ostatnia_skladka = models.PositiveIntegerField()
    status = models.CharField(max_length=50)
    uwagi = models.TextField(blank=True)

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"

    def is_past_due_medical(self):
    	return date.today() > self.nastepne_badanie

    def is_past_due_insurance(self):
    	return date.today() > self.ubezpieczenie

    def is_soon_past_due_medical(self):
    	return date.today() > (self.nastepne_badanie - timedelta(days=30))

    def is_soon_past_due_insurance (self):
    	return date.today() > (self.ubezpieczenie - timedelta(days=30))

class Pojazdy(models.Model):
    marka = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    typ = models.CharField(max_length=30)
    numer_rej = models.CharField(max_length=10)
    ubezpieczenie = models.DateField()
    ostatni_wyjazd = models.DateField()
    status = models.CharField(max_length=50)
    stan = models.CharField(max_length=50)
    uwagi = models.TextField(blank=True)

    def __str__(self):
        return f"{self.marka}, {self.model}, {self.numer_rej}"

    def is_past_due(self):
    	return date.today() > self.ubezpieczenie

    def is_soon_past_due(self):
    	return date.today() > (self.ubezpieczenie - timedelta(days=30))


class PrzegladPojazdy(models.Model):
    ostatni_przeglad = models.DateField()
    nastepny_przeglad = models.DateField()
    ostatnia_wymiana_olej_filtr = models.DateField()
    przebieg_przywymianie = models.PositiveIntegerField()
    mechanik = models.ForeignKey(Strazacy, related_name='mechanik_pojazdy', on_delete=models.CASCADE)
    uwagi = models.TextField(blank=True)
    pojazd = models.ForeignKey(Pojazdy, related_name='przeglad_pojazdy', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.pojazd} ({self.ostatni_przeglad} - {self.nastepny_przeglad})"

    def is_past_due(self):
    	return date.today() > self.nastepny_przeglad

    def is_soon_past_due(self):
    	return date.today() > (self.nastepny_przeglad - timedelta(days=30))


class PrzegladSprzet(models.Model):
    ostatni_przeglad = models.DateField()
    nastepny_przeglad = models.DateField(blank=True)
    mechanik = models.ForeignKey(Strazacy, related_name='mechanik_sprzet', on_delete=models.CASCADE)
    uwagi = models.TextField(blank=True)
    sprzet = models.ForeignKey(Sprzet, related_name='przeglad_sprzet', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.sprzet} ({self.ostatni_przeglad} - {self.nastepny_przeglad})"

    def is_past_due(self):
    	return date.today() > self.nastepny_przeglad

    def is_soon_past_due(self):
    	return date.today() > (self.nastepny_przeglad - timedelta(days=30))


class Uslugi(models.Model):
    usluga = models.CharField(max_length=300)
    nazwa_firmy = models.CharField(max_length=100)
    adres_firmy = models.CharField(max_length=300)
    miasto = models.CharField(max_length=30)
    tel_kontaktowy = models.PositiveIntegerField()
    termin_waznosci = models.DateField()
    termin_oplaty = models.DateField()
    kwota = models.DecimalField(max_digits=8, decimal_places=2)
    osoba_odpowiedzialna = models.ForeignKey(Strazacy, related_name='uslugi_osoby', on_delete=models.CASCADE)
    uwagi = models.TextField(blank=True)

    def __str__(self):
        return f"{self.usluga}, {self.nazwa_firmy}, {self.adres_firmy}"

    def is_past_due_validity(self):
    	return date.today() > self.termin_waznosci

    def is_past_due_payment(self):
    	return date.today() > self.termin_oplaty

    def is_soon_past_due_validity(self):
    	return date.today() > (self.termin_waznosci - timedelta(days=30))

    def is_soon_past_due_payment(self):
    	return date.today() > (self.termin_oplaty - timedelta(days=30))


class Uwaga(models.Model):
    class Status(Enum):
        NEW = auto()
        DONE = auto()
        REJECTED = auto()

    content = models.TextField()
    author = models.ForeignKey(get_user_model(), on_delete=models.SET_NULL, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.PositiveSmallIntegerField(choices=((status.value, status.name) for status in Status), default=Status.NEW.value)

    class Meta:
        abstract = True

class UwagaSprzet(Uwaga):
    subject = models.ForeignKey(Sprzet, on_delete=models.CASCADE)

    def get_url(self):
        return reverse('equipment-detail', args=(self.subject.pk,))

class UwagaStrazacy(Uwaga):
    subject = models.ForeignKey(Strazacy, on_delete=models.CASCADE)

    def get_url(self):
        return reverse('firefighter-detail', args=(self.subject.pk,))

class UwagaPojazdy(Uwaga):
    subject = models.ForeignKey(Pojazdy, on_delete=models.CASCADE)

    def get_url(self):
        return reverse('vehicle-detail', args=(self.subject.pk,))

class UwagaUslugi(Uwaga):
    subject = models.ForeignKey(Uslugi, on_delete=models.CASCADE)

    def get_url(self):
        return reverse('service-detail', args=(self.subject.pk,))

class UwagaPrzegladSprzet(Uwaga):
    subject = models.ForeignKey(PrzegladSprzet, on_delete=models.CASCADE)

    def get_url(self):
        return reverse('service-detail', args=(self.subject.pk,))

class UwagaPrzegladPojazdy(Uwaga):
    subject = models.ForeignKey(PrzegladPojazdy, on_delete=models.CASCADE)

    def get_url(self):
        return reverse('service-detail', args=(self.subject.pk,))
