# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-01-05 13:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gui', '0004_auto_20171227_1059'),
    ]

    operations = [
        migrations.AddField(
            model_name='equipment',
            name='mrl_1',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='equipment',
            name='mrl_2',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterUniqueTogether(
            name='equipment',
            unique_together=set([('mrl_1', 'mrl_2')]),
        ),
    ]