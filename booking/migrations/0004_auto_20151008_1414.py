# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0003_auto_20151008_1412'),
    ]

    operations = [
        migrations.RenameField(
            model_name='delegate',
            old_name='id',
            new_name='id_ticket',
        ),
    ]
