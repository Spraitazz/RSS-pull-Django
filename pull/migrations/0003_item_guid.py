# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pull', '0002_auto_20150901_1632'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='guid',
            field=models.CharField(max_length=63, default=0, unique=True),
            preserve_default=False,
        ),
    ]
