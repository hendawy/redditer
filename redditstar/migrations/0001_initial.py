# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='StarModel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('email', models.EmailField(max_length=254)),
                ('listing', models.CharField(max_length=20)),
            ],
            options={
                'verbose_name': 'StarModel',
                'verbose_name_plural': 'StarModel',
            },
        ),
        migrations.AlterUniqueTogether(
            name='starmodel',
            unique_together=set([('email', 'listing')]),
        ),
    ]
