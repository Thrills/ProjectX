# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('papers', '0003_auto_20151002_1051'),
    ]

    operations = [
        migrations.RenameField(
            model_name='author',
            old_name='author_country',
            new_name='country',
        ),
        migrations.RenameField(
            model_name='author',
            old_name='author_email',
            new_name='email',
        ),
        migrations.RenameField(
            model_name='author',
            old_name='author_institution',
            new_name='institution',
        ),
        migrations.RenameField(
            model_name='committeemember',
            old_name='cm_email',
            new_name='email',
        ),
        migrations.RenameField(
            model_name='committeemember',
            old_name='cm_institution',
            new_name='institution',
        ),
        migrations.RenameField(
            model_name='paper',
            old_name='paper_abstract',
            new_name='abstract',
        ),
        migrations.RenameField(
            model_name='paper',
            old_name='paper_language',
            new_name='language',
        ),
        migrations.RenameField(
            model_name='reviewer',
            old_name='reviewer_email',
            new_name='email',
        ),
        migrations.RenameField(
            model_name='reviewer',
            old_name='reviewer_institution',
            new_name='institution',
        ),
    ]
