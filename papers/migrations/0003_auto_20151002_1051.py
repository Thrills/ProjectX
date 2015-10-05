# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('papers', '0002_auto_20150928_1355'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paper',
            name='paper_submissionDate',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
