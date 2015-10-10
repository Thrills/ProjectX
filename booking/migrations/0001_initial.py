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
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('delegate_name', models.CharField(max_length=30)),
                ('delegate_surname', models.CharField(max_length=30)),
                ('institution', models.CharField(blank=True, max_length=50)),
                ('country', models.CharField(blank=True, max_length=50)),
                ('dietary_requirements', models.CharField(blank=True, choices=[('Vegetarian', 'Vegetarian'), ('Vegan', 'Vegan'), ('Halal', 'Halal'), ('Kosher', 'Kosher'), ('Gluten-free', 'Gluten-free'), ('Lactose-free', 'Lactose-free'), ('Shellfish-free', 'Shellfish-free'), ('Diabetic', 'Diabetic')], max_length=20)),
                ('other_requirements', models.CharField(blank=True, max_length=200)),
                ('email', models.EmailField(max_length=50)),
            ],
        ),
    ]
