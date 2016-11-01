# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_auto_20161029_1734'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='modified_at',
        ),
    ]
