# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('name', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=50)),
                ('date', models.DateTimeField(null=True)),
                ('doctor', models.CharField(max_length=50)),
                ('symptoms', models.CharField(max_length=500)),
                ('available', models.BooleanField()),
            ],
        ),
    ]
