# Generated by Django 4.0.4 on 2022-04-30 20:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app', '0010_letter_created_by_letter_created_date_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='letter',
            name='updated_by',
        ),
        migrations.RemoveField(
            model_name='person',
            name='updated_by',
        ),
        migrations.RemoveField(
            model_name='personprison',
            name='updated_by',
        ),
        migrations.RemoveField(
            model_name='prison',
            name='last_updated',
        ),
        migrations.RemoveField(
            model_name='prison',
            name='updated_by',
        ),
        migrations.AddField(
            model_name='letter',
            name='modified_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='letter_modified_by_user', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='person',
            name='modified_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='person_modified_by_user', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='personprison',
            name='modified_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='personprison_modified_by_user', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='prison',
            name='modified_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='prison_modified_by_user', to=settings.AUTH_USER_MODEL),
        ),
    ]
