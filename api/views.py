from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import Tanks
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

@api_view(['GET'])
def getTankEngines(request):
    tank_id = request.GET['tank_id']
    engines = Engines.objects.filter(tank_id = tank_id)
    serializer = TankEnginesSerializer(engines, many = True)
    return Response(serializer.data) 

@api_view(['GET'])
def getTankSuspensions(request):
    tank_id = request.GET['tank_id']
    suspensions = Suspensions.objects.filter(tank_id = tank_id)
    serializer = TankSuspensionsSerializer(suspensions, many = True)
    return Response(serializer.data) 

@api_view(['GET'])
def getTankTurrets(request):
    tank_id = request.GET['tank_id']
    turrets = Turrets.objects.filter(tank_id = tank_id)
    serializer = TankTurretsSerializer(turrets, many = True)
    return Response(serializer.data) 
