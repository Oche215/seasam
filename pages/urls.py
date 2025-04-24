from django.urls import path
from .views import (home, about, contact, mineral, mineral_detail, search, minerals, mineral_description, mb,
                    ss, sw, nw, ne, se, log, contract)

urlpatterns = [

    path('mineral/', mineral, name='mineral'),
    path('mineral_detail/<int:pk>', mineral_detail, name='mineral_detail'),
    path('search/', search, name='search'),
    path('minerals/', minerals, name='minerals'),
    path('mineral_description/<int:pk>', mineral_description, name='mineral_description'),

    path('mb/', mb, name='mb'),
    path('ss/', ss, name='ss'),
    path('sw/', sw, name='sw'),
    path('nw/', nw, name='nw'),
    path('ne/', ne, name='ne'),
    path('se/', se, name='se'),

    path('contract/', contract, name='contract'),
    path('logistics/', log, name='logistics'),
    path('contact/', contact, name='contact'),
    path('about/', about, name='about'),
    path('', home, name='home'),
]