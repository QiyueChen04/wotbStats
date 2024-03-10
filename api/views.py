from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Tanks
from .serializer import TankSerializer

@api_view(['GET'])
def getAllTanks(request):
    tanks = Tanks.objects.all()
    serializer = TankSerializer(tanks, many=True)
    return Response(serializer.data)