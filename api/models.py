# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Shark(models.Model):
    name = models.CharField(max_length=100)

        # Returns the string representation of the model.
    def __unicode__(self):              # __unicode__ on Python 2
        return str(self.name)

class Ping(models.Model):
    timestamp = models.DateTimeField()
    shark = models.ForeignKey(Shark, related_name='pings')
    latitude = models.FloatField()
    longitude = models.FloatField()

    def __unicode__(self):
        return unicode(self.shark.name + "-" + str(self.timestamp))

    def __str__(self):
        return unicode(self.shark.name + "-" + str(self.timestamp))