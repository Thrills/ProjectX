import datetime

from django.db import models
from django.utils import timezone


class Delegate(models.Model):
    DELEGATE_DIETARYREQUIREMENTS = (
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
    delegate_institution = models.CharField(max_length=50)
    delegate_country = models.CharField(max_length=50)
    delegate_dietaryRequirements = models.CharField(max_length=200, choices=DELEGATE_DIETARYREQUIREMENTS)
    delegate_email = models.EmailField(max_length=50)
    delegate_ticketNumber = models.IntegerField(max_length=3)


class Ticket(models.Model):
    TicketNumber = models.ForeignKey(Delegate)


