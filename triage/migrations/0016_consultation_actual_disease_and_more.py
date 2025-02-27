# Generated by Django 4.1.7 on 2023-05-10 21:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        (
            "triage",
            "0015_rename_timestamp_registered_consultation_datetime_registered_and_more",
        ),
    ]

    operations = [
        migrations.AddField(
            model_name="consultation",
            name="actual_disease",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="triage.disease",
            ),
        ),
        migrations.AddField(
            model_name="consultation",
            name="actual_urgency",
            field=models.IntegerField(blank=True, max_length=1, null=True),
        ),
        migrations.AddField(
            model_name="consultation",
            name="blood_pressure_diastolic",
            field=models.IntegerField(blank=True, max_length=3, null=True),
        ),
        migrations.AddField(
            model_name="consultation",
            name="blood_pressure_systolic",
            field=models.IntegerField(blank=True, max_length=3, null=True),
        ),
        migrations.AddField(
            model_name="consultation",
            name="hearthrate",
            field=models.IntegerField(blank=True, max_length=3, null=True),
        ),
        migrations.AddField(
            model_name="consultation",
            name="length",
            field=models.IntegerField(blank=True, max_length=3, null=True),
        ),
        migrations.AddField(
            model_name="consultation",
            name="objective",
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="consultation",
            name="saturation",
            field=models.IntegerField(blank=True, max_length=3, null=True),
        ),
        migrations.AddField(
            model_name="consultation",
            name="subjective",
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="consultation",
            name="temperature",
            field=models.FloatField(blank=True, max_length=3, null=True),
        ),
        migrations.AddField(
            model_name="consultation",
            name="weight",
            field=models.FloatField(blank=True, max_length=6, null=True),
        ),
        migrations.AlterField(
            model_name="consultation",
            name="datetime_end_consultation",
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="consultation",
            name="datetime_start_consultation",
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
