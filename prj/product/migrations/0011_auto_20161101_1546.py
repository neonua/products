# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0010_auto_20161101_1541'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime.now, editable=False),
        ),
        migrations.AlterField(
            model_name='product',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime.now, null=True, editable=False),
        ),
        migrations.AlterField(
            model_name='product',
            name='modified_at',
            field=models.DateTimeField(default=datetime.datetime.now, null=True, blank=True),
        ),
    ]
