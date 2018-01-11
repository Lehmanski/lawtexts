# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-01-07 14:22
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demo', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Equipment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('mrl', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(3)])),
            ],
        ),
    ]
