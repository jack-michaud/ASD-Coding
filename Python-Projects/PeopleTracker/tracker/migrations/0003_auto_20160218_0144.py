# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-02-18 01:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0002_auto_20160218_0124'),
    ]

    operations = [
        migrations.AddField(
            model_name='class',
            name='course_number',
            field=models.CharField(default='DJ100', max_length=20),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='class',
            name='room_per1',
            field=models.CharField(max_length=3, null=True),
        ),
        migrations.AlterField(
            model_name='class',
            name='room_per2',
            field=models.CharField(max_length=3, null=True),
        ),
        migrations.AlterField(
            model_name='class',
            name='room_per3',
            field=models.CharField(max_length=3, null=True),
        ),
        migrations.AlterField(
            model_name='class',
            name='room_per4',
            field=models.CharField(max_length=3, null=True),
        ),
        migrations.AlterField(
            model_name='class',
            name='room_per5',
            field=models.CharField(max_length=3, null=True),
        ),
        migrations.AlterField(
            model_name='class',
            name='room_per6',
            field=models.CharField(max_length=3, null=True),
        ),
        migrations.AlterField(
            model_name='class',
            name='room_per7',
            field=models.CharField(max_length=3, null=True),
        ),
        migrations.AlterField(
            model_name='class',
            name='room_per8',
            field=models.CharField(max_length=3, null=True),
        ),
    ]
