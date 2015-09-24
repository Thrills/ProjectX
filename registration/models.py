import datetime

from django.db import models
from django.utils import timezone


class Delegate(models.Model):
    dietary = (
	('Vegetarian'),
	('Vegan'),
	('Halal'),
	('Kosher'),
	('Gluten-free'),
	('Lactose-free'),
	('Shellfish-free'),
	('Diabetic'),
    )	 
    delegate_name = models.CharField(max_length=30)
    delegate_surname = models.CharField(max_length=30)
    delegate_institution = models.CharField(max_length=50,blank=True)
    delegate_country = models.CharField(max_length=50, blank=True )
    delegate_dietaryRequirements = models.CharField(max_length=20, choices=dietary, blank=True )
    delegate_otherRequirements = models.CharField(max_length=200, blank=True )
    delegate_email = models.EmailField(max_length=50, primary_key=True)
    delegate_ticketNumber = models.IntegerField(max_length=3)


class Ticket(models.Model):
    TicketNumber = models.ForeignKey(Delegate)


