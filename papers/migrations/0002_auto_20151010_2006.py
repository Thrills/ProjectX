# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('papers', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='paper',
            name='user',
        ),
        migrations.AddField(
            model_name='paper',
            name='username',
            field=models.CharField(default=0, max_length=100),
            preserve_default=False,
        ),
    ]
