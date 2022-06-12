# Generated by Django 4.0.4 on 2022-05-15 21:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0015_deprecated_prison_data_migration'),
    ]

    operations = [
        migrations.RenameField(
            model_name='prison',
            old_name='external_id',
            new_name='legacy_id',
        ),
        migrations.AlterField(
            model_name='letter',
            name='notes',
            field=models.CharField(blank=True, default='', max_length=200),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='prison',
            name='notes',
            field=models.CharField(blank=True, default='', max_length=200),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='prison',
            name='restrictions',
            field=models.CharField(blank=True, default='', max_length=200),
            preserve_default=False,
        ),
    ]
