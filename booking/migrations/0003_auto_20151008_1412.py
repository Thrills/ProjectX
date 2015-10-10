# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0002_auto_20150930_0959'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='delegate',
            name='ticket_number',
        ),
        migrations.AddField(
            model_name='delegate',
            name='id',
            field=models.AutoField(default=0, primary_key=True, serialize=False),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='delegate',
            name='email',
            field=models.EmailField(max_length=50),
        ),
    ]
