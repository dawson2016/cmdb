# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Audit',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('proname', models.CharField(max_length=30)),
                ('proenv', models.CharField(max_length=30)),
                ('status', models.IntegerField(verbose_name=2)),
                ('comment', models.CharField(max_length=30)),
            ],
        ),
    ]
