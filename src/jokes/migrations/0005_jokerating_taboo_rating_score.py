# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jokes', '0004_auto_20150529_2125'),
    ]

    operations = [
        migrations.AddField(
            model_name='jokerating',
            name='taboo_rating_score',
            field=models.PositiveSmallIntegerField(null=True, blank=True),
        ),
    ]
