# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jokes', '0002_joke_approved'),
    ]

    operations = [
        migrations.AddField(
            model_name='jokerating',
            name='age',
            field=models.PositiveSmallIntegerField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='jokerating',
            name='gender',
            field=models.PositiveSmallIntegerField(null=True, blank=True),
        ),
    ]
