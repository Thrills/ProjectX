# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('papers', '0008_auto_20151007_1335'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='paper_code',
            field=models.ForeignKey(to='papers.Paper'),
        ),
    ]
