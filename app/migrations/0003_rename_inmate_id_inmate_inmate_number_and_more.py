# Generated by Django 4.0.4 on 2022-04-23 21:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_inmateprison'),
    ]

    operations = [
        migrations.RenameField(
            model_name='inmate',
            old_name='inmate_id',
            new_name='inmate_number',
        ),
        migrations.RenameField(
            model_name='prison',
            old_name='prison_name',
            new_name='name',
        ),
    ]