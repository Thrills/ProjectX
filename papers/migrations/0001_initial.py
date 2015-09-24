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
                ('author_id', models.CharField(serialize=False, primary_key=True, max_length=10)),
                ('author_institution', models.CharField(max_length=50)),
                ('author_country', models.CharField(blank=True, max_length=50)),
                ('author_email', models.EmailField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Chairperson',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('cp_username', models.CharField(max_length=30)),
                ('cp_password', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='CommitteeMember',
            fields=[
                ('cm_name', models.CharField(max_length=30)),
                ('cm_surname', models.CharField(serialize=False, primary_key=True, max_length=30)),
                ('cm_institution', models.CharField(max_length=50)),
                ('cm_email', models.EmailField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Paper',
            fields=[
                ('paper_authorNames', models.CharField(max_length=100)),
                ('paper_submissionDate', models.DateTimeField(auto_now_add=True)),
                ('paper_submissionUpdate', models.DateTimeField(auto_now=True)),
                ('paper_abstract', models.CharField(max_length=300)),
                ('paper_language', models.CharField(max_length=20)),
                ('paper_code', models.CharField(serialize=False, primary_key=True, max_length=10)),
                ('paper_reviewCode', models.CharField(max_length=10)),
                ('paper_avgScore', models.CharField(null=True, blank=True, max_length=2)),
                ('paper_accepted', models.NullBooleanField()),
                ('author_id', models.ForeignKey(to='papers.Author')),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('review_score', models.CharField(max_length=2)),
                ('review_reviewCode', models.CharField(serialize=False, primary_key=True, max_length=10)),
                ('review_paperCode', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Reviewer',
            fields=[
                ('reviewer_name', models.CharField(max_length=30)),
                ('reviewer_surname', models.CharField(max_length=30)),
                ('reviewer_id', models.CharField(serialize=False, primary_key=True, max_length=10)),
                ('reviewer_institution', models.CharField(max_length=50)),
                ('reviewer_email', models.EmailField(max_length=50)),
                ('reviewer_paperCode', models.CharField(max_length=10)),
                ('reviewer_reviewCode', models.CharField(null=True, blank=True, max_length=10)),
            ],
        ),
        migrations.AddField(
            model_name='review',
            name='reviewer_id',
            field=models.ForeignKey(to='papers.Reviewer'),
        ),
    ]
