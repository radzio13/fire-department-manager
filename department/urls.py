from django.urls import path

from . import views

urlpatterns = [
    path('', views.HomeListView.as_view(), name='home'),
    
    path('sprzet/', views.EquipmentListView.as_view(), name='equipment-list'),
    path('sprzet/nowy/', views.EquipmentCreateView.as_view(), name='equipment-create'),
    path('sprzet/<int:pk>/', views.EquipmentDetailView.as_view(), name='equipment-detail'),
    path('sprzet/<int:pk>/edycja/', views.EquipmentUpdateView.as_view(), name='equipment-update'),
    path('sprzet/<int:pk>/usun/', views.EquipmentDeleteView.as_view(), name='equipment-delete'),

    path('pojazdy/', views.VehicleListView.as_view(), name='vehicle-list'),
    path('pojazdy/nowy/', views.VehicleCreateView.as_view(), name='vehicle-create'),
    path('pojazdy/<int:pk>/', views.VehicleDetailView.as_view(), name='vehicle-detail'),
    path('pojazdy/<int:pk>/edycja/', views.VehicleUpdateView.as_view(), name='vehicle-update'),
    path('pojazdy/<int:pk>/usun/', views.VehicleDeleteView.as_view(), name='vehicle-delete'),

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
]
