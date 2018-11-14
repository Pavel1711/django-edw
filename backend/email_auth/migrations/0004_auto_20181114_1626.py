# -*- coding: utf-8 -*-
# Generated by Django 1.9.13 on 2018-11-14 13:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('email_auth', '0003_bannedemaildomain'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='bannedemaildomain',
            options={'ordering': ('domain_name',), 'verbose_name': 'Banned email domain', 'verbose_name_plural': 'Banned email domains'},
        ),
        migrations.AlterField(
            model_name='bannedemaildomain',
            name='domain_name',
            field=models.CharField(db_index=True, max_length=255, unique=True, verbose_name='Domain name'),
        ),
    ]
