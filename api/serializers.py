from rest_framework import serializers
from .models import Tanks
from .models import Guns
from .models import Turrets
from .models import Engines
from .models import Suspensions

class AllTanksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tanks
        fields = "tank_id", "tank_name", "image_preview", "is_premium", "tier", "tank_type"

class TankSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tanks
        fields = '__all__'

class TankGunsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Guns
        fields = '__all__'

class TankEnginesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Engines
        fields = '__all__'

class TankSuspensionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Suspensions
        fields = '__all__'

class TankTurretsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Turrets
        fields = '__all__'
