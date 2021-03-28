
from django.conf.urls import url
from . import views
from django.urls import path

urlpatterns = [
    path('home/',
         views.HomePage.as_view(),
         name='home_page'),

]