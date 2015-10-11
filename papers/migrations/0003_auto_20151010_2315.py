# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('papers', '0002_auto_20151010_2006'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='username',
            field=models.CharField(default=0, max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='review',
            name='paper_code',
            field=models.CharField(max_length=100),
        ),
    ]
