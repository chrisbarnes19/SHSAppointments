# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appt', '0002_userprofile'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='appointment',
            name='email',
        ),
        migrations.RemoveField(
            model_name='appointment',
            name='name',
        ),
        migrations.AddField(
            model_name='appointment',
            name='user_profile',
            field=models.ForeignKey(to='appt.UserProfile', blank=True, null=True),
        ),
    ]
