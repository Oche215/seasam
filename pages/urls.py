from django.urls import path
from .views import home, about, contact, mineral, mineral_detail, search, ne, se, mb, ss, sw, nw, minerals, mineral_description


urlpatterns = [

    path('minerals/', minerals, name='minerals'),
    path('mineral_description/<int:pk>', mineral_description, name='mineral_description'),

    path('nw/', nw, name='nw'),
    path('sw/', sw, name='sw'),
    path('ss/', ss, name='ss'),
    path('mb/', mb, name='mb'),
    path('se/', se, name='se'),
    path('ne/', ne, name='ne'),

    path('search/', search, name='search'),
    path('mineral_detail/<int:pk>', mineral_detail, name='mineral_detail'),
    path('mineral/', mineral, name='mineral'),
    path('contact/', contact, name='contact'),
    path('about/', about, name='about'),
    path('', home, name='home'),
]