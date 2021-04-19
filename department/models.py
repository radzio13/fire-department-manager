from django.db import models
from django.contrib.auth.models import User
    
class Sprzet(models.Model):
    nazwa = models.CharField(max_length=300)
    marka = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    parametry = models.TextField(blank = True)
    rok_prod = models.PositiveIntegerField()
    status = models.CharField(max_length=50)
    stan = models.CharField(max_length=50)
    uwagi = models.TextField(blank = True)
    
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
    kierowca = models.BooleanField(default=False)
    termin_prawa_jazdy = models.DateField(blank=True)
    termin_wkladki = models.DateField(blank=True)
    termin_kpp = models.DateField(blank=True)
    ostatnia_skladka = models.PositiveIntegerField()
    status = models.CharField(max_length=50)
    uwagi = models.TextField(blank = True)
    
class Pojazdy(models.Model):
    marka = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    typ = models.CharField(max_length=30)
    numer_rej = models.CharField(max_length=10)
    ubezpieczenie = models.DateField()
    ostatni_wyjazd = models.DateField()
    status = models.CharField(max_length=50)
    stan = models.CharField(max_length=50)
    uwagi = models.TextField(blank = True)
    
class PrzegladPojazdy(models.Model):
    ostatni_przeglad = models.DateField()
    nastepny_przeglad = models.DateField()
    ostatnia_wymiana_olej_filtr = models.DateField()
    przebieg_przywymianie = models.PositiveIntegerField()
    mechanik = models.ForeignKey(Strazacy, related_name='mechanik_pojazdy', on_delete=models.CASCADE)
    uwagi = models.TextField(blank = True)
    pojazd = models.ForeignKey(Pojazdy, related_name='przeglad_pojazdy', on_delete=models.CASCADE)
    
class PrzegladSprzet(models.Model):
    ostatni_przeglad = models.DateField()
    nastepny_przeglad = models.DateField(blank=True)
    mechanik = models.ForeignKey(Strazacy, related_name='mechanik_sprzet', on_delete=models.CASCADE)
    uwagi = models.TextField(blank = True)
    sprzet = models.ForeignKey(Sprzet, related_name='przeglad_sprzet', on_delete=models.CASCADE)
    
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
    uwagi = models.TextField(blank = True)