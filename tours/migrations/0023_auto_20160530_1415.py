# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-30 11:15
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tours', '0022_auto_20160530_0918'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tour',
            options={'ordering': ['-start_date'], 'verbose_name': 'Тур', 'verbose_name_plural': 'Туры'},
        ),
    ]
