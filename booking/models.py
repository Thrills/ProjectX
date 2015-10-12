from django.db import models


class Delegate(models.Model):  # The database for delegates who have made a booking
    id = models.AutoField(primary_key=True)
    dietary = (  # Provides delegate with a specific choice
                 ('Vegetarian', 'Vegetarian'),
                 ('Vegan', 'Vegan'),
                 ('Halal', 'Halal'),
                 ('Kosher', 'Kosher'),
                 ('Gluten-free', 'Gluten-free'),
                 ('Lactose-free', 'Lactose-free'),
                 ('Shellfish-free', 'Shellfish-free'),
                 ('Diabetic', 'Diabetic'),
                 )
    delegate_name = models.CharField(max_length=30)
    delegate_surname = models.CharField(max_length=30)
    institution = models.CharField(max_length=50, blank=True)
    #blank set to True allows the database to have no value
    country = models.CharField(max_length=50, blank=True)
    dietary_requirements = models.CharField(max_length=20, choices=dietary, blank=True)
    other_requirements = models.CharField(max_length=200, blank=True)
    email = models.EmailField(max_length=50)

    def __str__(self):
        return '%s' % (self.id)



