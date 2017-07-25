# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='customer_address',
            field=models.CharField(max_length=128, blank=True, null=True, default=None),
        ),
        migrations.AddField(
            model_name='order',
            name='total_price',
            field=models.DecimalField(max_digits=10, decimal_places=2, default=0),
        ),
        migrations.AddField(
            model_name='productinorder',
            name='nmb',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='productinorder',
            name='price_per_item',
            field=models.DecimalField(max_digits=10, decimal_places=2, default=0),
        ),
        migrations.AddField(
            model_name='productinorder',
            name='total_price',
            field=models.DecimalField(max_digits=10, decimal_places=2, default=0),
        ),
    ]
