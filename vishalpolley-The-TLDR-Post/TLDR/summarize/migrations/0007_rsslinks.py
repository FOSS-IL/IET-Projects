# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-10-09 13:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('summarize', '0006_summary_source'),
    ]

    operations = [
        migrations.CreateModel(
            name='RSSlinks',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rss_link', models.URLField()),
                ('rss_title', models.TextField(default='', null=True)),
            ],
        ),
    ]
