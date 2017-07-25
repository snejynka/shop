# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('customer_name', models.CharField(default=None, max_length=64, null=True, blank=True)),
                ('customer_email', models.EmailField(default=None, max_length=254, null=True, blank=True)),
                ('customer_phone', models.CharField(default=None, max_length=48, null=True, blank=True)),
                ('comments', models.TextField(default=None, null=True, blank=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name_plural': 'Заказы',
                'verbose_name': 'Заказ',
            },
        ),
        migrations.CreateModel(
            name='ProductInOrder',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('is_active', models.BooleanField(default=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('order', models.ForeignKey(to='orders.Order', default=None, blank=True, null=True)),
                ('product', models.ForeignKey(to='products.Product', default=None, blank=True, null=True)),
            ],
            options={
                'verbose_name_plural': 'Товары',
                'verbose_name': 'Товар',
            },
        ),
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('name', models.CharField(default=None, max_length=24, null=True, blank=True)),
                ('is_active', models.BooleanField(default=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name_plural': 'Статусы заказа',
                'verbose_name': 'Статус заказа',
            },
        ),
        migrations.AddField(
            model_name='order',
            name='status',
            field=models.ForeignKey(to='orders.Status'),
        ),
    ]
