# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0007_like'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='like',
            name='comment',
        ),
        migrations.AddField(
            model_name='like',
            name='product',
            field=models.ForeignKey(default=b'', to='product.Product'),
        ),
    ]
