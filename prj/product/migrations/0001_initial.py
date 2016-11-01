# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=64, verbose_name='Name')),
                ('slug', models.SlugField(max_length=64)),
                ('description', models.TextField(verbose_name='Description')),
                ('price', models.FloatField(verbose_name='Price')),
                ('created_at', models.DateField()),
                ('modified_at', models.DateField()),
            ],
            options={
                'verbose_name': 'Product',
                'verbose_name_plural': 'Products',
            },
        ),
    ]
