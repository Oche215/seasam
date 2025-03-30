from django.urls import path
from .views import ConnectViewSet


urlpatterns = [

    path('', ConnectViewSet.as_view(), name='price'),
]