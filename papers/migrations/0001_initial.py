# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('author_name', models.CharField(max_length=30)),
                ('author_surname', models.CharField(max_length=30)),
                ('author_id', models.CharField(serialize=False, max_length=10, primary_key=True)),
                ('author_institution', models.CharField(max_length=50)),
                ('author_country', models.CharField(max_length=50, blank=True)),
                ('author_email', models.EmailField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Chairperson',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('cp_username', models.CharField(max_length=30)),
                ('cp_password', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='CommitteeMember',
            fields=[
                ('cm_id', models.CharField(serialize=False, max_length=3, primary_key=True)),
                ('cm_name', models.CharField(max_length=30)),
                ('cm_surname', models.CharField(max_length=30)),
                ('cm_institution', models.CharField(max_length=50)),
                ('cm_email', models.EmailField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Paper',
            fields=[
                ('paper_submissionDate', models.DateTimeField()),
                ('paper_abstract', models.CharField(max_length=300)),
                ('paper_language', models.CharField(max_length=20)),
                ('paper_code', models.CharField(serialize=False, max_length=10, primary_key=True)),
                ('paper_avgScore', models.CharField(null=True, max_length=2, blank=True)),
                ('paper_accepted', models.NullBooleanField()),
                ('author_id', models.ForeignKey(to='papers.Author')),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('review_score', models.CharField(max_length=2)),
                ('paper_code', models.ForeignKey(to='papers.Paper')),
            ],
        ),
        migrations.CreateModel(
            name='Reviewer',
            fields=[
                ('reviewer_name', models.CharField(max_length=30)),
                ('reviewer_surname', models.CharField(max_length=30)),
                ('reviewer_id', models.CharField(serialize=False, max_length=10, primary_key=True)),
                ('reviewer_institution', models.CharField(max_length=50)),
                ('reviewer_email', models.EmailField(max_length=50)),
                ('paper_code', models.ForeignKey(to='papers.Paper')),
            ],
        ),
        migrations.AddField(
            model_name='review',
            name='reviewer_id',
            field=models.ForeignKey(to='papers.Reviewer'),
        ),
    ]
