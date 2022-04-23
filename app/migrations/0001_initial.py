# Generated by Django 4.0.4 on 2022-04-23 20:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Inmate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('inmate_id', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Prison',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prison_name', models.CharField(max_length=200)),
            ],
        ),
    ]
