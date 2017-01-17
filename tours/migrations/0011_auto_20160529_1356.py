# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-05-29 10:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tours', '0010_auto_20160529_1323'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='date',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Дата публикации'),
        ),
        migrations.AlterField(
            model_name='review',
            name='text',
            field=models.CharField(blank=True, max_length=500, null=True, verbose_name='Текст'),
        ),
    ]