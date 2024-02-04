from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from extApi.models import Tank
from .serializer import TankSerializer

@api_view(['GET'])
def getTest(request):
    tanks = Tank.objects.all()
    serializer = TankSerializer(tanks, many=True)
    return Response(serializer.data)