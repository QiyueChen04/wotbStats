from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Tanks
from .serializers import AllTanksSerializer
from .serializers import TankSerializer

@api_view(['GET'])
def getAllTanks(request):
    tanks = Tanks.objects.values("tank_id", "tank_name", "image_preview", "is_premium", "tier", "tank_type")
    serializer = AllTanksSerializer(tanks, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getTankInfo(request):
    tank_id = request.GET['tank_id']
    tank = Tanks.objects.filter(tank_id = tank_id)
    serializer = TankSerializer(tank, many=True)
    return Response(serializer.data) 
