# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Candidate',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=250)),
                ('upvote', models.IntegerField(max_length=250)),
                ('downvote', models.IntegerField(max_length=250)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
