# Generated by Django 4.0.4 on 2022-04-30 20:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app', '0009_alter_personprison_current'),
    ]

    operations = [
        migrations.AddField(
            model_name='letter',
            name='created_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='letter_created_by_user', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='letter',
            name='created_date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='letter',
            name='modified_date',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='letter',
            name='updated_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='letter_updated_by_user', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='person',
            name='created_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='person_created_by_user', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='person',
            name='created_date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='person',
            name='modified_date',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='person',
            name='updated_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='person_updated_by_user', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='personprison',
            name='created_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='personprison_created_by_user', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='personprison',
            name='created_date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='personprison',
            name='modified_date',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='personprison',
            name='updated_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='personprison_updated_by_user', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='prison',
            name='created_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='prison_created_by_user', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='prison',
            name='created_date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='prison',
            name='modified_date',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='prison',
            name='updated_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='prison_updated_by_user', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='personprison',
            name='current',
            field=models.BooleanField(default=False),
        ),
    ]
