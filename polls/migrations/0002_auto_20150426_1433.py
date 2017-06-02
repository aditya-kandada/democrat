# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='candidate',
            name='first_name',
            field=models.CharField(max_length=100, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='candidate',
            name='last_name',
            field=models.CharField(max_length=100, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='candidate',
            name='downvote',
            field=models.IntegerField(max_length=250, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='candidate',
            name='upvote',
            field=models.IntegerField(max_length=250, null=True),
            preserve_default=True,
        ),
    ]
