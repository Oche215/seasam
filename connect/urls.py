from django.urls import path
from .views import ConnectViewSet, lct


urlpatterns = [

    path('', ConnectViewSet.as_view(), name='price'),
    path('contact/lcttechnologieslimited/', lct, name='lct'),

]