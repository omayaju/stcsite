# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-05-30 17:12
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('shop', '0003_good_warhouse'),
    ]

    operations = [
        migrations.CreateModel(
            name='GoodApp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.IntegerField(null=True, verbose_name='Количество заказываемого товара')),
                ('country', models.CharField(choices=[('Россия', 'Россия'), ('Белоруссияя', 'Белоруссия'), ('Азербайджан', 'Азербайджан'), ('Казахстан', 'Казахстан'), ('Армения', 'Армения')], max_length=200, null=True, verbose_name='Страна')),
                ('district', models.CharField(max_length=200, null=True, verbose_name='Область')),
                ('town', models.CharField(max_length=200, null=True, verbose_name='Город')),
                ('addres', models.CharField(max_length=200, null=True, verbose_name='Адрес улицы/дома')),
                ('email', models.EmailField(blank=True, max_length=200, null=True, verbose_name='E-mail')),
                ('phone', models.CharField(blank=True, max_length=200, null=True, verbose_name='Контактный телефон')),
                ('parent_good', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='shop.Good')),
                ('parent_user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Заказ',
                'verbose_name_plural': 'Заказы',
            },
        ),
    ]
