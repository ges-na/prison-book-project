# Generated by Django 4.1.2 on 2022-11-12 22:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0040_person_eligibility_bool"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="person",
            name="eligibility_bool",
        ),
        migrations.AddField(
            model_name="person",
            name="eligibility_status",
            field=models.CharField(
                choices=[
                    ("eligible", "Eligible"),
                    ("eligible, letters pending", "Pending"),
                    ("ineligible", "Ineligible"),
                ],
                default="eligible",
                max_length=200,
            ),
        ),
    ]