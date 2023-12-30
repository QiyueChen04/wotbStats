from django.shortcuts import render
from django.http import HttpResponse
import requests
from .models import Tanks

def save_api_response(request):
    url = 'https://api.wotblitz.com/wotb/encyclopedia/vehicles/?application_id=c6cb8f261ef9988cb66ea9a5d1271a60&fields=tank_id%2C+name%2C+images.preview%2C+images.normal'
    response = requests.get(url)

    if response.status_code == 200:
        api_data = response.json()

        for tank in api_data['data'].values():
            model_instance = Tanks(
                tank_id = tank['tank_id'],
                name = tank['name'],
                image_preview = tank['images']['preview'],
                image_normal = tank['images']['normal']
            )
            model_instance.save()

        return HttpResponse("Data saved")
    else:
        return HttpResponse("Fialed to fetch data")

def already_saved_extApi_response(request):
    return HttpResponse("Already saved wotb api response to database")