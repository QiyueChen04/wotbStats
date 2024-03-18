from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Tanks
from .serializer import TankSerializer

@api_view(['GET'])
def getAllTanks(request):
    tanks = Tanks.objects.values("tank_id", "tank_name", "image_preview", "is_premium", "tier", "tank_type")
    serializer = TankSerializer(tanks, many=True)
    return Response(serializer.data)
