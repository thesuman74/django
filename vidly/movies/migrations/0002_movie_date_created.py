# Generated by Django 5.0.3 on 2024-03-27 15:17

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2024, 3, 27, 15, 17, 16, 34939, tzinfo=datetime.timezone.utc)),
        ),
    ]
