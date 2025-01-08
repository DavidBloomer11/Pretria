# Generated by Django 4.1.7 on 2023-05-10 14:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        (
            "triage",
            "0014_rename_maximum_length_openaimodelconfiguration_max_tokens_and_more",
        ),
    ]

    operations = [
        migrations.RenameField(
            model_name="consultation",
            old_name="timestamp_registered",
            new_name="datetime_registered",
        ),
        migrations.AddField(
            model_name="consultation",
            name="datetime_end_consultation",
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name="consultation",
            name="datetime_start_consultation",
            field=models.DateTimeField(null=True),
        ),
    ]
