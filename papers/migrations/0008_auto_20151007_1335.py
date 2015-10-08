# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('papers', '0007_auto_20151007_1235'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='paper_code',
            field=models.ForeignKey(unique=True, to='papers.Paper'),
        ),
    ]
