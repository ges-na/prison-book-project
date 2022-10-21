# Generated by Django 4.0.5 on 2022-09-25 19:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0035_alter_prison_modified_date'),
    ]

    operations = [
        migrations.RenameField(
            model_name='letter',
            old_name='processed_date',
            new_name='stage1_complete_date',
        ),
        migrations.AddField(
            model_name='prison',
            name='accepts_books',
            field=models.CharField(choices=[(True, 'True'), (False, 'False'), (None, 'Unknown')], default=None, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='prison',
            name='additional_mailing_headers',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='letter',
            name='workflow_stage',
            field=models.CharField(choices=[('stage1_complete', 'Stage 1 complete'), ('awaiting_fulfillment', 'Awaiting fulfillment'), ('fulfilled', 'Fulfilled'), ('just_pada', 'Just PADA'), ('problem', 'Problem')], default='stage1_complete', max_length=200),
        ),
    ]
