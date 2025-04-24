from django.urls import path
from .views import maps

urlpatterns = [
    path('', maps, name='map'),
]