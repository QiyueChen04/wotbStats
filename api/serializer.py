from rest_framework import serializers
from .models import Tanks

class TankSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tanks
        fields = "tank_id", "tank_name", "image_preview", "is_premium", "tier", "tank_type"
