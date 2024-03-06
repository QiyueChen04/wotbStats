from django.db import models

class Suspension(models.Model):
    module_id = models.IntegerField(primary_key = True)
    traverse_speed = models.IntegerField(blank = True, null = True) 
    weight = models.IntegerField(blank = True, null = True) 

    def __str__(self):
        return self.module_id
 

class Engine(models.Model):
    module_id = models.IntegerField(primary_key = True)
    engine_power = models.IntegerField(blank = True, null = True) 
    fire_chance = models.FloatField(blank = True, null = True) 
    weight = models.IntegerField(blank = True, null = True) 

    def __str__(self):
        return self.module_id


class Turret(models.Model):
    module_id = models.IntegerField(primary_key = True)
    view_range = models.IntegerField(blank = True, null = True) 
    front = models.IntegerField(blank = True, null = True)
    sides = models.IntegerField(blank = True, null = True) 
    rear = models.IntegerField(blank = True, null = True) 
    hp = models.IntegerField(blank = True, null = True) 
    traverse_right_arc = models.IntegerField(blank = True, null = True) 
    traverse_left_arc = models.IntegerField(blank = True, null = True) 

    def __str__(self):
        return self.module_id 


class Gun(models.Model):
    module_id = models.IntegerField(primary_key = True)
    type1 = models.CharField(max_length = 255, blank = True, null = True)
    pen1 = models.IntegerField(blank = True, null = True)
    dmg1 = models.IntegerField(blank = True, null = True) 
    type2 = models.CharField(max_length = 255, blank = True, null = True)
    pen2 = models.IntegerField(blank = True, null = True)
    dmg2 = models.IntegerField(blank = True, null = True) 
    type3 = models.CharField(max_length = 255, blank = True, null = True)
    pen3 = models.IntegerField(blank = True, null = True)
    dmg3 = models.IntegerField(blank = True, null = True) 
    dispersion = models.FloatField(blank = True, null = True) 
    aim_time = models.FloatField(blank = True, null = True) 

    def __str__(self):
        return self.module_id  


class Tank(models.Model):
    tank_id = models.IntegerField(primary_key = True)
    name = models.CharField(max_length = 255, blank = True, null = True)
    image_preview = models.CharField(max_length = 255, blank = True, null = True)
    image_normal = models.CharField(max_length = 255, blank = True, null = True)
    nation = models.CharField(max_length = 255, blank = True, null = True)
    is_premium = models.IntegerField(blank = True, null = True)
    tier = models.IntegerField(blank = True, null = True)
    type = models.CharField(max_length=255, blank = True, null = True)

    front = models.IntegerField(blank = True, null = True)
    sides = models.IntegerField(blank = True, null = True)
    rear = models.IntegerField(blank = True, null = True)

    speed_forward = models.IntegerField(blank = True, null = True)
    speed_backward = models.IntegerField(blank = True, null = True)
    
    hp = models.IntegerField(blank = True, null = True)

    move_down_arc = models.IntegerField(blank = True, null = True)
    move_up_arc = models.IntegerField(blank = True, null = True)
    caliber = models.IntegerField(blank = True, null = True)
    fire_rate = models.FloatField(blank = True, null = True)
    reload_time = models.FloatField(blank = True, null = True) 
    clip_capacity = models.IntegerField(blank = True, null = True)
    clip_reload_time = models.FloatField(blank = True, null = True) 

    gun_traverse_speed = models.FloatField(blank = True, null = True) 
    turret_traverse_speed = models.IntegerField(blank = True, null = True)
    hull_hp = models.IntegerField(blank = True, null = True) 

    suspensions = models.ManyToManyField(Suspension)
    engines = models.ManyToManyField(Engine)
    turrets = models.ManyToManyField(Turret)
    guns = models.ManyToManyField(Gun)

    def __str__(self):
        return self.tank_id
