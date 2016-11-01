# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0011_auto_20161101_1546'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='like',
            options={'verbose_name': 'Who liked', 'verbose_name_plural': 'Who liked'},
        ),
    ]
