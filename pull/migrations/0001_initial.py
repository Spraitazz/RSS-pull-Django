# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('title', models.CharField(max_length=255)),
                ('url', models.CharField(max_length=255)),
                ('description', models.CharField(max_length=65535)),
                ('date', models.DateTimeField(verbose_name='date')),
            ],
        ),
    ]
