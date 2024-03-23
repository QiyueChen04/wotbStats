from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import Tanks
from .models import TankGuns
from .models import TankTurrets
from .models import TankEngines
from .models import TankSuspensions
from .models import Guns
from .models import Turrets
from .models import Engines
from .models import Suspensions

from .serializers import *

@api_view(['GET'])
def getAllTanks(request):
    tanks = Tanks.objects.values("tank_id", "tank_name", "image_preview", "is_premium", "tier", "tank_type")
    serializer = AllTanksSerializer(tanks, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getTank(request):
    tank_id = request.GET['tank_id']
    tank = Tanks.objects.filter(tank_id = tank_id)
    serializer = TankSerializer(tank, many=True)
    return Response(serializer.data) 

@api_view(['GET'])
def getTankGuns(request):
    tank_id = request.GET['tank_id']
    guns = Guns.objects.filter(tank_id = tank_id)
    serializer = TankGunsSerializer(guns, many = True)
    return Response(serializer.data) 
