# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models

class Tanks(models.Model):
    tank_id = models.IntegerField(primary_key=True)
    tank_name = models.CharField(max_length=100, blank=True, null=True)
    image_preview = models.CharField(max_length=200, blank=True, null=True)
    image_normal = models.CharField(max_length=200, blank=True, null=True)
    nation = models.CharField(max_length=20, blank=True, null=True)
    is_premium = models.CharField(max_length=1, blank=True, null=True)
    tier = models.SmallIntegerField(blank=True, null=True)
    tank_type = models.CharField(max_length=20, blank=True, null=True)
    front = models.SmallIntegerField(blank=True, null=True)
    sides = models.SmallIntegerField(blank=True, null=True)
    rear = models.SmallIntegerField(blank=True, null=True)
    speed_forward = models.SmallIntegerField(blank=True, null=True)
    speed_backward = models.SmallIntegerField(blank=True, null=True)
    hp = models.SmallIntegerField(blank=True, null=True)
    move_down_arc = models.SmallIntegerField(blank=True, null=True)
    move_up_arc = models.SmallIntegerField(blank=True, null=True)
    caliber = models.SmallIntegerField(blank=True, null=True)
    fire_rate = models.FloatField(blank=True, null=True)
    reload_time = models.FloatField(blank=True, null=True)
    clip_capacity = models.SmallIntegerField(blank=True, null=True)
    clip_reload_time = models.FloatField(blank=True, null=True)
    gun_traverse_speed = models.FloatField(blank=True, null=True)
    turret_traverse_speed = models.SmallIntegerField(blank=True, null=True)
    hull_hp = models.SmallIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tanks'

#__________________________________________________________________________________________
class Guns(models.Model):
    module_id = models.IntegerField(primary_key=True)
    type1 = models.CharField(max_length=20, blank=True, null=True)
    pen1 = models.SmallIntegerField(blank=True, null=True)
    dmg1 = models.SmallIntegerField(blank=True, null=True)
    type2 = models.CharField(max_length=20, blank=True, null=True)
    pen2 = models.SmallIntegerField(blank=True, null=True)
    dmg2 = models.SmallIntegerField(blank=True, null=True)
    type3 = models.CharField(max_length=20, blank=True, null=True)
    pen3 = models.SmallIntegerField(blank=True, null=True)
    dmg3 = models.SmallIntegerField(blank=True, null=True)
    dispersion = models.FloatField(blank=True, null=True)
    aim_time = models.FloatField(blank=True, null=True)

    tank_id = models.ManyToManyField(
        Tanks,
        through='TankGuns',
        through_fields=('module', 'tank')
    )

    class Meta:
        managed = False
        db_table = 'guns'

class TankGuns(models.Model):
    pair_id = models.IntegerField(primary_key = True)
    tank = models.ForeignKey(Tanks, models.DO_NOTHING)
    module = models.ForeignKey(Guns, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'tankguns'

#__________________________________________________________________________________________
class Engines(models.Model):
    module_id = models.IntegerField(primary_key=True)
    engine_power = models.SmallIntegerField(blank=True, null=True)
    fire_chance = models.FloatField(blank=True, null=True)
    weight = models.IntegerField(blank=True, null=True)

    tank_id = models.ManyToManyField(
        Tanks,
        through='TankEngines',
        through_fields=('module', 'tank')
    )

    class Meta:
        managed = False
        db_table = 'engines'

class TankEngines(models.Model):
    pair_id = models.IntegerField(primary_key = True)
    tank = models.ForeignKey(Tanks, models.DO_NOTHING)  
    module = models.ForeignKey(Engines, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'tankengines'
#__________________________________________________________________________________________
class Suspensions(models.Model):
    module_id = models.IntegerField(primary_key=True)
    traverse_speed = models.SmallIntegerField(blank=True, null=True)
    weight = models.SmallIntegerField(blank=True, null=True)

    tank_id = models.ManyToManyField(
        Tanks,
        through='TankSuspensions',
        through_fields=('module', 'tank')
    )

    class Meta:
        managed = False
        db_table = 'suspensions'


class TankSuspensions(models.Model):
    pair_id = models.IntegerField(primary_key = True)
    tank = models.ForeignKey(Tanks, models.DO_NOTHING)  
    module = models.ForeignKey(Suspensions, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'tanksuspensions'

#__________________________________________________________________________________________

class Turrets(models.Model):
    module_id = models.IntegerField(primary_key=True)
    view_range = models.SmallIntegerField(blank=True, null=True)
    front = models.SmallIntegerField(blank=True, null=True)
    sides = models.SmallIntegerField(blank=True, null=True)
    rear = models.SmallIntegerField(blank=True, null=True)
    hp = models.SmallIntegerField(blank=True, null=True)
    traverse_right_arc = models.SmallIntegerField(blank=True, null=True)
    traverse_left_arc = models.SmallIntegerField(blank=True, null=True)

    tank_id = models.ManyToManyField(
        Tanks,
        through='TankTurrets',
        through_fields=('module', 'tank')
    )

    class Meta:
        managed = False
        db_table = 'turrets'

class TankTurrets(models.Model):
    pair_id = models.IntegerField(primary_key = True)
    tank = models.ForeignKey(Tanks, models.DO_NOTHING)  
    module = models.ForeignKey(Turrets, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'tankturrets'

#__________________________________________________________________________________________

class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'
