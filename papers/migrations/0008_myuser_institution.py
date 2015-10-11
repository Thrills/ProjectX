# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('papers', '0007_auto_20151011_0930'),
    ]

    operations = [
        migrations.AddField(
            model_name='myuser',
            name='institution',
            field=models.CharField(max_length=50, default=0),
            preserve_default=False,
        ),
    ]
