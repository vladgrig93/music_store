# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-10-26 22:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login_app', '0007_auto_20171026_2000'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='recorditems',
            field=models.ManyToManyField(related_name='order_item', through='login_app.RecordItem', to='login_app.Record'),
        ),
    ]