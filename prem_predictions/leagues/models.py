from django.db import models
from django_countries.fields import CountryField
from django.core.validators import MaxValueValidator

class league(models.Model):
    """
    A model to display group the teams into their respective divisions
    """
    name = models.CharField(max_length=100)
    friendly_name = models.CharField(max_length=100, null=True, blank=True)
    
    def __str__(self):
        return f'{self.name}'

    def get_friendly_name(self):
        return f'{self.friendly_name}'
    
class team(models.Model):
    """
    A model to collect the individual info for each team
    """
    name = models.CharField(max_length=250)
    friendly_name = models.CharField(max_length=250, null=True, blank=True)
    country = CountryField()
    league = models.ForeignKey(league, on_delete=models.CASCADE)
    games_played = models.PositiveSmallIntegerField(
        validators=[MaxValueValidator(38)],
        default=0
    )
    wins = models.PositiveSmallIntegerField(
        validators=[MaxValueValidator(38)],
        default=0
    )
    draws = models.PositiveSmallIntegerField(
        validators=[MaxValueValidator(38)],
        default=0
    )
    losses = models.PositiveSmallIntegerField(
        validators=[MaxValueValidator(38)],
        default=0
    )
    goals_for = models.PositiveSmallIntegerField(default=0)
    goals_against = models.PositiveSmallIntegerField(default=0)
    goal_difference = models.SmallIntegerField(default=0)
    points = models.SmallIntegerField(default=0)