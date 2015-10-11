# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('papers', '0008_myuser_institution'),
    ]

    operations = [
        migrations.AddField(
            model_name='myuser',
            name='country',
            field=models.CharField(default=0, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='myuser',
            name='role',
            field=models.CharField(default=0, max_length=20),
            preserve_default=False,
        ),
    ]
