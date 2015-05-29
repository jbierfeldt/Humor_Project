# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jokes', '0003_auto_20150529_1614'),
    ]

    operations = [
        migrations.AlterField(
            model_name='joke',
            name='approved',
            field=models.BooleanField(default=False),
        ),
    ]
