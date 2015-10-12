# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('papers', '0009_auto_20151011_1055'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='review',
            options={'permissions': ()},
        ),
    ]
