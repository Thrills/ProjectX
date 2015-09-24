# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='delegate',
            name='delegate_dietaryRequirements',
            field=models.CharField(max_length=20, blank=True, choices=[('Vegetarian', 'Vegetarian'), ('Vegan', 'Vegan'), ('Halal', 'Halal'), ('Kosher', 'Kosher'), ('Gluten-free', 'Gluten-free'), ('Lactose-free', 'Lactose-free'), ('Shellfish-free', 'Shellfish-free'), ('Diabetic', 'Diabetic')]),
        ),
    ]
