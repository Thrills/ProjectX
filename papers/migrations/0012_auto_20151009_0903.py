# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('papers', '0011_auto_20151008_1412'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paper',
            name='abstract',
            field=models.TextField(max_length=300),
        ),
        migrations.AlterField(
            model_name='review',
            name='comments',
            field=models.TextField(max_length=300),
        ),
    ]
