# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pull', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='date',
            field=models.CharField(max_length=255),
        ),
    ]
