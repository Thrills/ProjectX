# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('papers', '0009_auto_20151007_1336'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='comments',
            field=models.CharField(max_length=300, default=0),
            preserve_default=False,
        ),
    ]
