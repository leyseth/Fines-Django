from django.db import models

class infraction(models.Model):
    street = models.CharField(max_length=30)
    speed_limit = models.CharField(max_length=30)
    infractions_speed = models.CharField(max_length=30)
