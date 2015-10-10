# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0005_auto_20151008_1415'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='delegate',
            name='id_ticket',
        ),
        migrations.AddField(
            model_name='delegate',
            name='id',
            field=models.AutoField(serialize=False, primary_key=True, default=0),
            preserve_default=False,
        ),
    ]
