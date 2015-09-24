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
                ('delegate_dietaryRequirements', models.CharField(choices=[('Vegetarian', ''), ('Vegan', ''), ('Halal', ''), ('Kosher', ''), ('Gluten-free', ''), ('Lactose-free', ''), ('Shellfish-free', ''), ('Diabetic', '')], max_length=20, blank=True)),
                ('delegate_otherRequirements', models.CharField(max_length=200, blank=True)),
                ('delegate_email', models.EmailField(serialize=False, max_length=50, primary_key=True)),
                ('delegate_ticketNumber', models.CharField(max_length=3)),
            ],
        ),
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('TicketNumber', models.ForeignKey(to='registration.Delegate')),
            ],
        ),
    ]
