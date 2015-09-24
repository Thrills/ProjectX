
from django.db import models


class Delegate(models.Model):  # The database for delegates who have made a booking

    dietary = (
	('Vegetarian','Vegetarian'),
	('Vegan','Vegan'),
	('Halal','Halal'),
	('Kosher','Kosher'),
	('Gluten-free','Gluten-free'),
	('Lactose-free','Lactose-free'),
	('Shellfish-free','Shellfish-free'),
	('Diabetic','Diabetic'),
    )	 
    delegate_name = models.CharField(max_length=30)
    delegate_surname = models.CharField(max_length=30)
    delegate_institution = models.CharField(max_length=50, blank=True)
    delegate_country = models.CharField(max_length=50, blank=True)
    delegate_dietaryRequirements = models.CharField(max_length=20, choices=dietary, blank=True)
    delegate_otherRequirements = models.CharField(max_length=200, blank=True)
    delegate_email = models.EmailField(max_length=50, primary_key=True)
    delegate_ticketNumber = models.CharField(max_length=3)

class Ticket(models.Model):
    TicketNumber = models.ForeignKey(Delegate)
