# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-01-15 13:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='description',
            field=models.TextField(blank=True, default=None, null=True),
        ),
    ]