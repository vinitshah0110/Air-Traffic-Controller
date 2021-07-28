from django.db import models
from django.core.validators import MinValueValidator
from atc.models import Runway, Atc
from flight.models import Flight

class Takeoff(models.Model):
    starting_atc    = models.ForeignKey(Atc, on_delete=models.CASCADE, related_name='tekeoff_atc')
    flight          = models.ForeignKey(Flight, on_delete=models.CASCADE, related_name='flight_takingoff')
    time            = models.DateTimeField()
    created_at      = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated_at      = models.DateTimeField(auto_now_add=False, auto_now=True)
    priority        = models.BooleanField(default=False)
    is_active       = models.BooleanField(default=True)

    def __str__(self):
        return self.starting_atc.name

class Landing(models.Model):
    ending_atc      = models.ForeignKey(Atc, on_delete=models.CASCADE, related_name='landing_runway')
    flight          =  models.ForeignKey(Flight, on_delete=models.CASCADE, related_name='flight_landing')
    time            = models.DateTimeField()
    created_at      = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated_at      = models.DateTimeField(auto_now_add=False, auto_now=True)
    priority        = models.BooleanField(default=False)
    is_active       = models.BooleanField(default=True)

    def __str__(self):
        return self.ending_atc.name