from rest_framework import serializers
from .models import Connect

class PriceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Connect
        fields = '__all__'