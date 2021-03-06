from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

from department.models import Strazacy, Pojazdy, Uslugi, Sprzet, PrzegladSprzet, PrzegladPojazdy


class FirefighterUpdateForm(forms.ModelForm):
    first_name = forms.CharField(required=True, max_length=150, label='Imie')
    last_name = forms.CharField(required=True, max_length=150, label='Nazwisko')
    username = forms.CharField(required=True, max_length=150, label='Nazwa użytkownika')
    email = forms.EmailField(required=True)

    class Meta:
        model = Strazacy
        fields = ('first_name', 'last_name', 'username', 'email', 'data_urodzenia', 'data_wstapienia',
                  'ostatnie_badanie', 'nastepne_badanie', 'ubezpieczenie', 'kierowca', 'termin_prawa_jazdy',
                  'termin_wkladki', 'termin_kpp', 'ostatnia_skladka', 'status', 'uwagi',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['first_name'].initial = self.instance.user.first_name
        self.fields['last_name'].initial = self.instance.user.last_name
        self.fields['username'].initial = self.instance.user.username
        self.fields['email'].initial = self.instance.user.email

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if User.objects.filter(username=username).exclude(pk=self.instance.pk).exists():
            raise ValidationError('Użytkownik z taką nazwą użytkownika już istnieje')
        return username


class FirefighterCreateForm(forms.ModelForm):
    first_name = forms.CharField(required=True, max_length=150, label='Imie')
    last_name = forms.CharField(required=True, max_length=150, label='Nazwisko')
    username = forms.CharField(required=True, max_length=150, label='Nazwa użytkownika')
    email = forms.EmailField(required=True)
    password = forms.CharField(required=True, max_length=128, label='Hasło',
                               widget=forms.PasswordInput(attrs={'autocomplete': 'current-password'}))
    password_repeat = forms.CharField(required=True, max_length=128, label='Powtórz hasło',
                                      widget=forms.PasswordInput(attrs={'autocomplete': 'current-password'}))

    class Meta:
        model = Strazacy
        fields = ('first_name', 'last_name', 'username', 'email', 'password', 'password_repeat', 'data_urodzenia',
                  'data_wstapienia', 'ostatnie_badanie', 'nastepne_badanie', 'ubezpieczenie', 'kierowca',
                  'termin_prawa_jazdy', 'termin_wkladki', 'termin_kpp', 'ostatnia_skladka', 'status', 'uwagi',)

    def clean(self):
        password = self.cleaned_data.get('password')
        password_repeat = self.cleaned_data.get('password_repeat')

        if password != password_repeat:
            raise ValidationError('Hasła muszą być takie same.', )
        return super().clean()

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if User.objects.filter(username=username).exists():
            raise ValidationError('Użytkownik z taką nazwą już istnieje')
        return username

class VehicleCreateForm(forms.ModelForm):

    class Meta:
        model = Pojazdy
        fields = '__all__'

class ServiceCreateForm(forms.ModelForm):
    
    class Meta:
        model = Uslugi
        fields = '__all__'
        
class EquipmentUpdateForm(forms.ModelForm):

	class Meta:
		model = Sprzet
		fields = ('nazwa', 'marka', 'model', 'parametry', 'rok_prod', 'status', 'stan', 'uwagi',)
		
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)


class EquipmentCreateForm(forms.ModelForm):
	
	class Meta:
		model = Sprzet
		fields = ('nazwa', 'marka', 'model', 'parametry', 'rok_prod', 'status', 'stan', 'uwagi',)
		
class HistoryEquipmentUpdateForm(forms.ModelForm):

	class Meta:
		model = PrzegladSprzet
		fields = ('sprzet', 'ostatni_przeglad', 'nastepny_przeglad', 'mechanik', 'uwagi',)
		
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)


class HistoryEquipmentCreateForm(forms.ModelForm):
	
	class Meta:
		model = PrzegladSprzet
		fields = ('sprzet', 'ostatni_przeglad', 'nastepny_przeglad', 'mechanik', 'uwagi')

class HistoryVehicleCreateForm(forms.ModelForm):

    class Meta:
        model = PrzegladPojazdy
        fields = '__all__'
