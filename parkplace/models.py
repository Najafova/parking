from django.db import models

class Place(models.Model):
    device_name = models.CharField(max_length = 100)
    status = models.CharField(max_length = 10)
    bronetime_start = models.DateTimeField(null=True,blank=True)
    bronetime_end = models.DateTimeField(null=True,blank=True)
    def __str__(self):
        return f'Parking place {self.device_name}'

class Data(models.Model):
    device_name = models.CharField(null=True, blank=True, max_length = 100)
    x_coordinate = models.IntegerField(null=True, blank=True, default=0)
    y_coordinate = models.IntegerField(null=True, blank=True, default=0)
    z_coordinate = models.IntegerField(null=True, blank=True, default=0)

class Reserves(models.Model):
    start_date  = models.DateTimeField()
    end_date = models.DateTimeField()
    to_place = models.ForeignKey(Place,on_delete=models.CASCADE)


class Log(models.Model):
    device_name = models.CharField(null=True, blank=True, max_length = 100)
    x_coordinate = models.IntegerField(null=True, blank=True, default=0)
    y_coordinate = models.IntegerField(null=True, blank=True, default=0)
    z_coordinate = models.IntegerField(null=True, blank=True, default=0)

