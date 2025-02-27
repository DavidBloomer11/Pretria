# Generated by Django 4.1.7 on 2023-04-22 23:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("triage", "0006_alter_encounter_gender"),
    ]

    operations = [
        migrations.AlterField(
            model_name="encounter",
            name="urgency_prediction",
            field=models.CharField(
                choices=[
                    ("routine", "Routine"),
                    ("niet urgent", "Niet urgent"),
                    ("dringend", "Dringend"),
                    ("spoed", "Spoed"),
                    ("levensbedreigend", "Levensbedreigend"),
                ],
                max_length=20,
                null=True,
            ),
        ),
    ]
