# Generated by Django 4.0.5 on 2022-07-13 03:46

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0021_person_legacy_prison_id_alter_letter_processed_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='legacy_last_served_date',
            field=models.DateTimeField(default=None, null=True),
        ),
        migrations.AlterField(
            model_name='letter',
            name='processed_date',
            field=models.DateField(blank=True, default=datetime.datetime(2022, 7, 12, 23, 46, 19, 266473), null=True),
        ),
    ]
