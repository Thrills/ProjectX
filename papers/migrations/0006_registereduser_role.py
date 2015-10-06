# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('papers', '0005_auto_20151006_1440'),
    ]

    operations = [
        migrations.AddField(
            model_name='registereduser',
            name='role',
            field=models.CharField(blank=True, choices=[('Author', 'Author'), ('Reviewer', 'Reviewer'), ('Commiteee Member', 'Commiteee Member')], max_length=20),
        ),
    ]
