# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('papers', '0004_auto_20151006_1030'),
    ]

    operations = [
        migrations.CreateModel(
            name='RegisteredUser',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=30)),
                ('surname', models.CharField(max_length=30)),
                ('institution', models.CharField(max_length=50)),
                ('country', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=50)),
            ],
        ),
        migrations.DeleteModel(
            name='Chairperson',
        ),
        migrations.DeleteModel(
            name='CommitteeMember',
        ),
        migrations.RemoveField(
            model_name='reviewer',
            name='paper_code',
        ),
        migrations.RemoveField(
            model_name='paper',
            name='author_id',
        ),
        migrations.RemoveField(
            model_name='review',
            name='reviewer_id',
        ),
        migrations.AlterField(
            model_name='paper',
            name='paper_code',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='review',
            name='id',
            field=models.ForeignKey(to='papers.RegisteredUser', serialize=False, primary_key=True),
        ),
        migrations.DeleteModel(
            name='Author',
        ),
        migrations.DeleteModel(
            name='Reviewer',
        ),
        migrations.AddField(
            model_name='paper',
            name='id',
            field=models.ForeignKey(to='papers.RegisteredUser', default=0),
            preserve_default=False,
        ),
    ]
