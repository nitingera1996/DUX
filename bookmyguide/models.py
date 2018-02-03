from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.core.validators import URLValidator

class DuxProfile(models.Model):
    user = models.OneToOneField(User)
    full_name = models.CharField(max_length=200)
    mobile_number = models.BigIntegerField()
    profile_photo = models.TextField(validators=[URLValidator()],blank=True)
    is_guide = models.BooleanField(default=False)

    def __unicode__(self):
        return "%s" %(self.full_name)

class Places(models.Model):
    name = models.CharField(max_length=200)
    average_time=models.BigIntegerField(default=30)
    price = models.BigIntegerField(blank=True)

    def __unicode__(self):
        return "%s" %(self.name)

class Guide(models.Model):
    dux_profile=models.OneToOneField(DuxProfile)
    sum_rating=models.BigIntegerField(default=5)
    number_of_rating = models.BigIntegerField(default=1)
    places = models.ManyToManyField(Places)
    id_card = models.TextField(validators=[URLValidator()],blank=True)
    address = models.TextField(blank=True)
    is_verified= models.BooleanField(default=False)
    
    def __unicode__(self):
        return "%s" %(self.dux_profile.full_name)


