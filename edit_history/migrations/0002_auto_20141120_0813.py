# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django_fsm


class Migration(migrations.Migration):

    dependencies = [
        ('edit_history', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='url',
            name='language',
            field=models.CharField(default='en', max_length=4),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='url',
            name='url',
            field=models.CharField(unique=True, default='http://en.wikipedia.com/test', max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='url',
            name='state',
            field=django_fsm.FSMField(choices=[('0', 'New'), ('1', 'Downloading'), ('2', 'Downloading'), ('3', 'Processing'), ('4', 'Processing'), ('5', 'Complete'), ('-1', 'Failed')], default='0', max_length=50),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='url',
            name='title',
            field=models.CharField(max_length=100),
            preserve_default=True,
        ),
    ]
