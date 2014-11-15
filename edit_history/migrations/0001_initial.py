# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django_fsm


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Url',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('title', models.CharField(max_length=100, unique=True)),
                ('state', django_fsm.FSMField(choices=[(0, 'New'), (1, 'Downloading'), (2, 'Processing'), (3, 'Complete'), (-1, 'Failed')], max_length=50, default=0)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
