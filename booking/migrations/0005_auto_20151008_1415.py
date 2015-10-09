# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0004_auto_20151008_1414'),
    ]

    operations = [
        migrations.AlterField(
            model_name='delegate',
            name='id_ticket',
            field=models.AutoField(unique=True, serialize=False, primary_key=True),
        ),
    ]
