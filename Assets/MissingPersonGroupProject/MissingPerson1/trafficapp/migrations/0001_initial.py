# Generated by Django 4.1.7 on 2023-04-07 19:29

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_missing', models.DateField(blank=True, default=datetime.datetime.today)),
                ('last_name', models.CharField(max_length=30)),
                ('first_name', models.CharField(max_length=30)),
                ('age_at_missing', models.IntegerField(default=0)),
                ('city', models.CharField(max_length=20)),
                ('state', models.CharField(max_length=20)),
                ('gender', models.CharField(max_length=100)),
                ('race', models.CharField(blank=True, max_length=13)),
            ],
        ),
    ]
