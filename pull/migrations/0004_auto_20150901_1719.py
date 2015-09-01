# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pull', '0003_item_guid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='guid',
            field=models.CharField(unique=True, max_length=63, default=0),
        ),
    ]
