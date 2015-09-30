from django.db import models


class Delegate(models.Model):  # The database for delegates who have made a booking

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
    country = models.CharField(max_length=50, blank=True)
    dietary_requirements = models.CharField(max_length=20, choices=dietary, blank=True)
    other_requirements = models.CharField(max_length=200, blank=True)
    email = models.EmailField(max_length=50, primary_key=True)
    ticket_number = models.CharField(max_length=3)

    def __str__(self):
        return '%s %s %s %s %s %s %s %s' % (self.delegate_name, self.delegate_surname, self.institution, self.country,
                                            self.dietary_requirements, self.other_requirements, self.email,
                                            self.ticket_number)


class Ticket(models.Model):
    ticket_number = models.ForeignKey(Delegate)

    def __str__(self):
        return self.ticket_number
