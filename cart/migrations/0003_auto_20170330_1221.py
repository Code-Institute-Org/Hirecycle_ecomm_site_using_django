# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-30 12:21
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0002_auto_20170329_2112'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cartitem',
            old_name='product',
            new_name='advert',
        ),
    ]
