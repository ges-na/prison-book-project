# Generated by Django 4.0.5 on 2022-08-08 04:45

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0034_alter_personprison_current_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prison',
            name='modified_date',
            field=models.DateTimeField(auto_now=True, default=datetime.datetime(2022, 8, 8, 0, 45, 16, 167643)),
            preserve_default=False,
        ),
    ]