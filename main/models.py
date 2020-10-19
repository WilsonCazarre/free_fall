from django.db import models
from django.contrib.auth.models import User

game_roles = [
    ('tank', 'Tank'),
    ('damage', 'Damage'),
    ('support', 'Support'),
]

competitive_modes = [
    ('role_q', 'Role Queue'),
    ('open_q', 'Open Queue')
]

game_modes = [
    ('assault', 'Assault'),
    ('control', 'Control (2 CP)'),
    ('escort', 'Escort'),
    ('hybrid', 'Hybrid'),
    ('push', 'Push')
]


class Profile(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    battle_tag = models.CharField
    damage_sr = models.IntegerField(null=True)
    tank_sr = models.IntegerField(null=True)
    support_sr = models.IntegerField(null=True)
    open_queue_sr = models.IntegerField(null=True)


class Hero(models.Model):
    name = models.CharField(max_length=50)
    portrait = models.ImageField(null=True)
    role = models.TextField(choices=game_roles)

    class Meta:
        verbose_name_plural = 'Heroes'


class GameMap(models.Model):
    name = models.CharField(max_length=50)
    game_mode = models.CharField(choices=game_modes, max_length=15)
    portrait = models.ImageField(null=True)


class Match(models.Model):
    profile_id = models.ForeignKey(Profile, on_delete=models.CASCADE)
    map_id = models.ForeignKey(GameMap, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    competitive_mode = models.CharField(choices=competitive_modes, max_length=10)
    played_role = models.CharField(choices=game_roles, max_length=10)
    new_sr = models.IntegerField

    class Meta:
        verbose_name_plural = 'Matches'


class PlayedHeroes(models.Model):
    match_id = models.ForeignKey(Match, on_delete=models.CASCADE)
    hero_id = models.ForeignKey(Hero, on_delete=models.CASCADE)
