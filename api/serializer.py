from rest_framework import serializers
from extApi.models import Tank

class TankSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tank
        fields = ('name', 'tier')