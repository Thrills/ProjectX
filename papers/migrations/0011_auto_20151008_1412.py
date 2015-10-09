# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('papers', '0010_review_comments'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='review_score',
            field=models.CharField(blank=True, max_length=2, choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10')]),
        ),
    ]
