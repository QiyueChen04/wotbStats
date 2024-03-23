from rest_framework import serializers
from .models import Tanks
from .models import TankGuns
from .models import TankTurrets
from .models import TankEngines
from .models import TankSuspensions
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