from datetime import datetime
from email.policy import default
from pickle import TRUE
from random import choices
import django
from django.db import models
from django_countries.fields import CountryField

# Create your models here.
class Contact(models.Model):
    docId = models.CharField(max_length=20)
    name = models.CharField(max_length=50)
    phone = models.CharField(max_length=20)
    email = models.CharField(max_length=50)

class Booking(models.Model):
    STATES = (
        ('p','Pendiente'),
        ('pr','En progreso'),
        ('f','Finalizado'),
        ('c','Cancelado')
    )
    contactId = models.ForeignKey(Contact, on_delete=models.CASCADE)
    state = models.CharField(max_length=20,choices=STATES)
    bookingDate = models.DateField(default=django.utils.timezone.now)
    price = models.FloatField(default=0)
    outstanding = models.FloatField(default=0)

class Traveler(models.Model):
    docId = models.CharField(max_length=20)
    fNames = models.CharField(max_length=50)
    lNames = models.CharField(max_length=50)
    country = CountryField()
    birth = models.DateField(default=django.utils.timezone.now)

class TravelerRegistry(models.Model):
    bookingId = models.ForeignKey(Booking, on_delete=models.CASCADE)
    travelerId = models.ForeignKey(Traveler, on_delete=models.DO_NOTHING)

class Tour(models.Model):
    tour = models.CharField(max_length=30)
    nDays = models.IntegerField(default=1)
    price = models.FloatField(default=0)

class TourRegistry(models.Model):
    bookingId = models.ForeignKey(Booking, on_delete=models.CASCADE)
    tourId = models.ForeignKey(Tour, on_delete=models.DO_NOTHING)


    