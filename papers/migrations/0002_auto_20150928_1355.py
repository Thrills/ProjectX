# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('papers', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reviewer',
            name='paper_code',
            field=models.ForeignKey(to='papers.Paper', null=True),
        ),
    ]
