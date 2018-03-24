from django.db import models

# Create your models here.

class Zipcode(models.Model):
    number = models.IntegerField(default=-1)
    vehicle_miles = models.IntegerField(default=0)
    
    def __str__(self):
        return "zip code: " + str(self.number)
    def lots_of_miles(self):
        return self.vehicle_miles > 10000