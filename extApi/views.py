from django.shortcuts import render
from django.http import HttpResponse
import requests
from .models import Tank
from .models import Suspension
from .models import Engine
from .models import Turret
from .models import Gun


# Fills the Suspension db table
def fill_suspension(request):
    url = 'https://api.wotblitz.com/wotb/encyclopedia/modules/?application_id=c6cb8f261ef9988cb66ea9a5d1271a60&fields=suspensions'
    response = requests.get(url)

    if response.status_code == 200:
        api_data = response.json()

        for suspension in api_data['data']['suspensions']:
            new_suspension = Suspension(
                module_id = suspension['module_id'],
                traverse_speed = suspension['traverse_speed'],
                weight = suspension['weight']
            )
            new_suspension.save()

        return HttpResponse("Data saved")
    else:
        return HttpResponse("Failed to fetch data")




# Fills the Engine db table
def fill_engine(request):
    url = 'https://api.wotblitz.com/wotb/encyclopedia/modules/?application_id=c6cb8f261ef9988cb66ea9a5d1271a60&fields=engines'
    response = requests.get(url)

    if response.status_code == 200:
        api_data = response.json()

        for engine in api_data['data']['engines']:
            new_engine = Engine(
                module_id = engine['module_id'],
                engine_power = engine['power'],
                fire_chance = engine['fire_chance'],
                weight = engine['weight']
            )
            new_engine.save()

        return HttpResponse("Data saved")
    else:
        return HttpResponse("Failed to fetch data")



# Fills the Turret db table
def fill_turret(request):
    url = 'https://api.wotblitz.com/wotb/encyclopedia/modules/?application_id=c6cb8f261ef9988cb66ea9a5d1271a60&fields=turrets'
    response = requests.get(url)

    if response.status_code == 200:
        api_data = response.json()

        for engine in api_data['data']['turrets']:
            new_turret = Turret(
                module_id = engine['module_id'],
                view_range = engine['view_range'],
                front = engine['armor']['front'],
                sides = engine['armor']['sides'],
                rear = engine['armor']['rear'],
                hp = engine['hp'],
                traverse_right_arc = engine['traverse_right_arc'],
                traverse_left_arc = engine['traverse_left_arc']
            )
            new_turret.save()

        return HttpResponse("Data saved")
    else:
        return HttpResponse("Failed to fetch data")


# Fills the Gun db table
def fill_gun(request):
    url = 'https://api.wotblitz.com/wotb/encyclopedia/modules/?application_id=c6cb8f261ef9988cb66ea9a5d1271a60&fields=guns'
    response = requests.get(url)
    if response.status_code == 200:
        api_data = response.json()
        for gun in api_data['data']['guns']:
            shells = gun['shells']
            if(len(shells) == 1):
                new_gun = Gun(
                    module_id = gun['module_id'],
                    dispersion = gun['dispersion'],
                    aim_time = gun['aim_time'],
                    type1 = shells[0]['type'],
                    pen1 = shells[0]['penetration'],
                    dmg1 = shells[0]['damage']
                )
            if(len(shells) == 2):
                new_gun = Gun(
                    module_id = gun['module_id'],
                    dispersion = gun['dispersion'],
                    aim_time = gun['aim_time'],
                    type1 = shells[0]['type'],
                    pen1 = shells[0]['penetration'],
                    dmg1 = shells[0]['damage'],
                    type2 = shells[1]['type'],
                    pen2 = shells[1]['penetration'],
                    dmg2 = shells[1]['damage'], 
                )
            if(len(shells) == 3):
                new_gun = Gun(
                    module_id = gun['module_id'],
                    dispersion = gun['dispersion'],
                    aim_time = gun['aim_time'],
                    type1 = shells[0]['type'],
                    pen1 = shells[0]['penetration'],
                    dmg1 = shells[0]['damage'],
                    type2 = shells[1]['type'],
                    pen2 = shells[1]['penetration'],
                    dmg2 = shells[1]['damage'], 
                    type3 = shells[2]['type'],
                    pen3 = shells[2]['penetration'],
                    dmg3 = shells[2]['damage'], 
                ) 
            new_gun.save()
        return HttpResponse("Data saved")
    else:
        return HttpResponse("Failed to fetch data")


# Fills ...

    tanks = Tank.objects.all()
    for tank in tanks:
        url = 'https://api.wotblitz.com/wotb/encyclopedia/vehicleprofile/?application_id=c6cb8f261ef9988cb66ea9a5d1271a60&tank_id=' + str(tank.tank_id)
        response = request.get(url)

        if response.status_code == 200:
            api_data = response.json()
            tank_char = api_data['data'][str(tank.tank_idk)]
            
        else:
            return HttpResponse("Failed to fetch data")

        

# Fills tank db table
def fill_tank(request):
    tank_url = 'https://api.wotblitz.com/wotb/encyclopedia/vehicles/?application_id=c6cb8f261ef9988cb66ea9a5d1271a60'
    tank_response = requests.get(tank_url)

    if tank_response.status_code == 200:
        tank_data = tank_response.json()
        for tank in tank_data['data'].values():
            char_url = 'https://api.wotblitz.com/wotb/encyclopedia/vehicleprofile/?application_id=c6cb8f261ef9988cb66ea9a5d1271a60&tank_id=' + str(tank['tank_id'])
            char_response = requests.get(char_url)
            char_data = char_response.json()
            char = char_data['data'][str(tank['tank_id'])]

            new_tank = Tank(
                tank_id = tank['tank_id'],
                name = tank['name'],
                image_preview = tank['images']['preview'],
                image_normal = tank['images']['normal'],
                nation = tank['nation'],
                is_premium = tank['is_premium'],
                tier = tank['tier'],
                type = tank['type'],

                front = char['armor']['hull']['front'],
                sides = char['armor']['hull']['sides'],
                rear = char['armor']['hull']['rear'],
                speed_forward = char['speed_forward'],
                speed_backward = char['speed_backward'],
                hp = char['hp'],
                move_down_arc = char['gun']['move_down_arc'],
                move_up_arc = char['gun']['move_up_arc'],
                caliber = char['gun']['caliber'],
                fire_rate = char['gun']['fire_rate'],
                reload_time = char['gun']['reload_time'],
                clip_capacity = char['gun']['clip_capacity'],
                clip_reload_time = char['gun']['clip_reload_time'],
                gun_traverse_speed = char['gun']['traverse_speed'],
                turret_traverse_speed = char['turret']['traverse_speed'],
                hull_hp = char['hull_hp'],
            )
            new_tank.save()
            new_tank.suspensions.set(tank['suspensions'])
            new_tank.engines.set(tank['engines'])
            new_tank.turrets.set(tank['turrets'])
            new_tank.guns.set(tank['guns'])
            
        return HttpResponse("Data saved")
    else:
        return HttpResponse("Failed to fetch data")

def already_saved_extApi_response(request):
    return HttpResponse("Already saved wotb api response to database tables")