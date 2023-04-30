# Generated by Django 4.1.2 on 2023-04-30 00:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0049_remove_personprison_current"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="letter",
            name="in_packing_pipeline_date",
        ),
        migrations.AlterField(
            model_name="letter",
            name="workflow_stage",
            field=models.CharField(
                choices=[
                    ("stage1_complete", "Stage 1 complete"),
                    ("fulfilled", "Fulfilled"),
                    ("just_pada", "Just PADA"),
                    ("problem", "Problem"),
                    ("discarded", "Discarded"),
                ],
                default="stage1_complete",
                max_length=200,
            ),
        ),
    ]
