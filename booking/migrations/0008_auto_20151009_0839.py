# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0007_auto_20151008_1425'),
    ]

    operations = [
        migrations.AlterField(
            model_name='delegate',
            name='id',
            field=models.AutoField(serialize=False, primary_key=True),
        ),
    ]
