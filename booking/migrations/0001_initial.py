# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Delegate',
            fields=[
                ('delegate_name', models.CharField(max_length=30)),
                ('delegate_surname', models.CharField(max_length=30)),
                ('delegate_institution', models.CharField(max_length=50, blank=True)),
                ('delegate_country', models.CharField(max_length=50, blank=True)),
                ('delegate_dietaryRequirements', models.CharField(choices=[('Vegetarian', 'Vegetarian'), ('Vegan', 'Vegan'), ('Halal', 'Halal'), ('Kosher', 'Kosher'), ('Gluten-free', 'Gluten-free'), ('Lactose-free', 'Lactose-free'), ('Shellfish-free', 'Shellfish-free'), ('Diabetic', 'Diabetic')], max_length=20, blank=True)),
                ('delegate_otherRequirements', models.CharField(max_length=200, blank=True)),
                ('delegate_email', models.EmailField(primary_key=True, serialize=False, max_length=50)),
                ('delegate_ticketNumber', models.CharField(max_length=3)),
            ],
        ),
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('TicketNumber', models.ForeignKey(to='booking.Delegate')),
            ],
        ),
    ]
