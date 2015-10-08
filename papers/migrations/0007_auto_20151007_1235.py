# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('papers', '0006_registereduser_role'),
    ]

    operations = [
        migrations.AddField(
            model_name='paper',
            name='paper_file',
            field=models.FileField(upload_to='paper_list/%Y/%m/%d', default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='paper',
            name='title',
            field=models.CharField(max_length=100, default=0),
            preserve_default=False,
        ),
    ]
