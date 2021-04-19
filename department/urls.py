from django.urls import path

from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('sprzet/', views.EquipmentView.as_view(), name='equipment')
]
