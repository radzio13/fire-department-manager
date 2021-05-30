from django.urls import path

from . import views
from .api import make_comment

urlpatterns = [
    path('', views.HomeListView.as_view(), name='home'),

    path('sprzet/', views.EquipmentListView.as_view(), name='equipment-list'),
    path('sprzet/nowy/', views.EquipmentCreateView.as_view(), name='equipment-create'),
    path('sprzet/<int:pk>/', views.EquipmentDetailView.as_view(), name='equipment-detail'),
    path('sprzet/<int:pk>/edycja/', views.EquipmentUpdateView.as_view(), name='equipment-update'),
    path('sprzet/<int:pk>/usun/', views.EquipmentDeleteView.as_view(), name='equipment-delete'),
    
    path('historia-sprzet/', views.HistoryEquipmentListView.as_view(), name='history-equipment-list'),
    path('historia-sprzet/nowy/', views.HistoryEquipmentCreateView.as_view(), name='history-equipment-create'),
    path('historia-sprzet/<int:pk>/', views.HistoryEquipmentDetailView.as_view(), name='history-equipment-detail'),
    path('historia-sprzet/<int:pk>/edycja/', views.HistoryEquipmentUpdateView.as_view(), name='history-equipment-update'),
    path('historia-sprzet/<int:pk>/usun/', views.HistoryEquipmentDeleteView.as_view(), name='history-equipment-delete'),

    path('pojazdy/', views.VehicleListView.as_view(), name='vehicle-list'),
    path('pojazdy/nowy/', views.VehicleCreateView.as_view(), name='vehicle-create'),
    path('pojazdy/<int:pk>/', views.VehicleDetailView.as_view(), name='vehicle-detail'),
    path('pojazdy/<int:pk>/edycja/', views.VehicleUpdateView.as_view(), name='vehicle-update'),
    path('pojazdy/<int:pk>/usun/', views.VehicleDeleteView.as_view(), name='vehicle-delete'),
    
    path('historia-pojazdy/', views.HistoryVehicleListView.as_view(), name='history-vehicle-list'),
    path('historia-pojazdy/nowy/', views.HistoryVehicleCreateView.as_view(), name='history-vehicle-create'),
    path('historia-pojazdy/<int:pk>/', views.HistoryVehicleDetailView.as_view(), name='history-vehicle-detail'),
    path('historia-pojazdy/<int:pk>/edycja/', views.HistoryVehicleUpdateView.as_view(), name='history-vehicle-update'),
    path('historia-pojazdy/<int:pk>/usun/', views.HistoryVehicleDeleteView.as_view(), name='history-vehicle-delete'),

    path('uslugi/', views.ServiceListView.as_view(), name='service-list'),
    path('uslugi/nowy/', views.ServiceCreateView.as_view(), name='service-create'),
    path('uslugi/<int:pk>/', views.ServiceDetailView.as_view(), name='service-detail'),
    path('uslugi/<int:pk>/edycja/', views.ServiceUpdateView.as_view(), name='service-update'),
    path('uslugi/<int:pk>/usun/', views.ServiceDeleteView.as_view(), name='service-delete'),

    path('strazacy/', views.FirefighterListView.as_view(), name='firefighter-list'),
    path('strazacy/nowy/', views.FirefighterCreateView.as_view(), name='firefighter-create'),
    path('strazacy/<int:pk>/', views.FirefighterDetailView.as_view(), name='firefighter-detail'),
    path('strazacy/<int:pk>/edycja/', views.FirefighterUpdateView.as_view(), name='firefighter-update'),
    path('strazacy/<int:pk>/usun/', views.FirefighterDeleteView.as_view(), name='firefighter-delete'),

    path('api/make-comment/', make_comment, name='make-comment'),
]
