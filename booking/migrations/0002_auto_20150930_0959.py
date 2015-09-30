# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='delegate',
            old_name='delegate_country',
            new_name='country',
        ),
        migrations.RenameField(
            model_name='delegate',
            old_name='delegate_dietaryRequirements',
            new_name='dietary_requirements',
        ),
        migrations.RenameField(
            model_name='delegate',
            old_name='delegate_email',
            new_name='email',
        ),
        migrations.RenameField(
            model_name='delegate',
            old_name='delegate_institution',
            new_name='institution',
        ),
        migrations.RenameField(
            model_name='delegate',
            old_name='delegate_otherRequirements',
            new_name='other_requirements',
        ),
        migrations.RenameField(
            model_name='delegate',
            old_name='delegate_ticketNumber',
            new_name='ticket_number',
        ),
        migrations.RenameField(
            model_name='ticket',
            old_name='TicketNumber',
            new_name='ticket_number',
        ),
    ]
