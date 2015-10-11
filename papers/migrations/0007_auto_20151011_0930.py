# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('papers', '0006_auto_20151011_0726'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paper',
            name='paper_file',
            field=models.FileField(upload_to='paper_list'),
        ),
    ]
