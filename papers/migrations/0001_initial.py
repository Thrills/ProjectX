# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MyUser',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('password', models.CharField(verbose_name='password', max_length=128)),
                ('last_login', models.DateTimeField(verbose_name='last login', blank=True, null=True)),
                ('username', models.CharField(unique=True, max_length=255)),
                ('email', models.EmailField(verbose_name='email address', unique=True, max_length=255)),
                ('first_name', models.CharField(max_length=120)),
                ('last_name', models.CharField(max_length=120)),
                ('is_author', models.BooleanField(verbose_name='Is an Author', default=True)),
                ('is_reviewer', models.BooleanField(verbose_name='Is a Reviewer', default=False)),
                ('is_cm', models.BooleanField(verbose_name='Is a Committee Member', default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('is_admin', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Paper',
            fields=[
                ('title', models.CharField(max_length=100)),
                ('paper_submissionDate', models.DateTimeField(auto_now_add=True)),
                ('abstract', models.TextField(max_length=300)),
                ('language', models.CharField(max_length=20)),
                ('paper_file', models.FileField(upload_to='paper_list/%Y/%m/%d')),
                ('paper_code', models.AutoField(primary_key=True, serialize=False)),
                ('paper_avgScore', models.CharField(blank=True, null=True, max_length=2)),
                ('paper_accepted', models.NullBooleanField()),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('review_score', models.CharField(blank=True, choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10')], max_length=2)),
                ('comments', models.TextField(max_length=300)),
                ('paper_code', models.ForeignKey(to='papers.Paper')),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
