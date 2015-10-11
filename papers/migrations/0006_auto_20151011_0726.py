# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('papers', '0005_auto_20151011_0710'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='paper_code',
            field=models.ForeignKey(to='papers.Paper'),
        ),
        migrations.AlterField(
            model_name='review',
            name='username',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
    ]
