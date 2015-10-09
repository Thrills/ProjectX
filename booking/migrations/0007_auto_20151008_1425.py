# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0006_auto_20151008_1418'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ticket',
            name='ticket_number',
        ),
        migrations.AlterField(
            model_name='delegate',
            name='id',
            field=models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True),
        ),
        migrations.DeleteModel(
            name='Ticket',
        ),
    ]
