# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_auto_20150426_1433'),
    ]

    operations = [
        migrations.AlterField(
            model_name='candidate',
            name='downvote',
            field=models.IntegerField(max_length=250, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='candidate',
            name='upvote',
            field=models.IntegerField(max_length=250, null=True, blank=True),
            preserve_default=True,
        ),
    ]
