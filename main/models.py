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
    ('assault', 'Assault (2 CP)'),
    ('control', 'Control'),
    ('escort', 'Escort'),
    ('hybrid', 'Hybrid'),
    ('push', 'Push')
]


class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    battle_tag = models.CharField
    damage_sr = models.IntegerField(null=True)
    tank_sr = models.IntegerField(null=True)
    support_sr = models.IntegerField(null=True)
    open_queue_sr = models.IntegerField(null=True)


class Hero(models.Model):
    name = models.CharField(max_length=50)
    portrait = models.ImageField(null=True, upload_to='hero_portraits')
    role = models.TextField(choices=game_roles)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Heroes'
        ordering = ('name',)


class GameMap(models.Model):
    name = models.CharField(max_length=50)
    game_mode = models.CharField(choices=game_modes, max_length=15)
    portrait = models.ImageField(null=True, upload_to='map_portraits')

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name',)


class Match(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    map = models.ForeignKey(GameMap, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    competitive_mode = models.CharField(choices=competitive_modes, max_length=10)
    played_role = models.CharField(choices=game_roles, max_length=10)
    new_sr = models.IntegerField

    class Meta:
        verbose_name_plural = 'Matches'


class PlayedHeroes(models.Model):
    match = models.ForeignKey(Match, on_delete=models.CASCADE)
    hero = models.ForeignKey(Hero, on_delete=models.CASCADE)
