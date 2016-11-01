# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0004_auto_20161030_0710'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='modified_at',
            field=models.DateField(auto_now=True, null=True),
        ),
    ]
