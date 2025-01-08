# Generated by Django 4.1.7 on 2023-04-14 18:49

from django.db import migrations, models
import django.db.models.deletion
import triage.models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ("triage", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Disease",
            fields=[
                ("disease_id", models.AutoField(primary_key=True, serialize=False)),
                ("name", models.CharField(max_length=1000)),
            ],
            options={
                "db_table": "disease",
                "managed": True,
            },
        ),
        migrations.CreateModel(
            name="DiseaseHasSymptom",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
            ],
            options={
                "db_table": "disease_has_symptom",
                "managed": True,
            },
        ),
        migrations.CreateModel(
            name="Encounter",
            fields=[
                ("timestamp", models.DateTimeField(auto_created=True, auto_now=True)),
                ("encounter_id", models.AutoField(primary_key=True, serialize=False)),
                (
                    "uuid",
                    models.UUIDField(default=uuid.uuid4, editable=False, unique=True),
                ),
                (
                    "follow_up_code",
                    models.CharField(
                        default=triage.models.Encounter.generate_code, max_length=8
                    ),
                ),
                (
                    "urgency_prediction",
                    models.CharField(
                        choices=[
                            ("routine", "Routine"),
                            ("niet urgent", "Niet urgent"),
                            ("dringend", "Dringend"),
                            ("spoed", "Spoed"),
                            ("levensbedreigend", "Levensbedreigend"),
                        ],
                        max_length=20,
                    ),
                ),
                ("description", models.CharField(max_length=1000)),
                ("age", models.IntegerField()),
                (
                    "gender",
                    models.CharField(
                        choices=[("male", "Male"), ("female", "Female")], max_length=10
                    ),
                ),
            ],
            options={
                "db_table": "Encounter",
                "managed": True,
            },
        ),
        migrations.CreateModel(
            name="EncounterDiseasePrediction",
            fields=[
                (
                    "encounter_diagnosis_prediction_id",
                    models.AutoField(primary_key=True, serialize=False),
                ),
                ("likelihood", models.IntegerField()),
                (
                    "disease",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="triage.disease"
                    ),
                ),
                (
                    "encounter",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="triage.encounter",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="EncounterFollowUp",
            fields=[
                (
                    "timestamp_registered",
                    models.DateTimeField(auto_created=True, auto_now=True),
                ),
                (
                    "encounter_follow_up_id",
                    models.AutoField(primary_key=True, serialize=False),
                ),
                (
                    "encounter",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="triage.encounter",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="EncounterQuestion",
            fields=[
                (
                    "encounter_question_id",
                    models.AutoField(primary_key=True, serialize=False),
                ),
                ("question", models.CharField(max_length=100)),
                ("answer", models.CharField(max_length=200)),
                ("answer_type", models.CharField(max_length=10)),
                (
                    "encounter",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="triage.encounter",
                    ),
                ),
            ],
            options={
                "db_table": "EncounterQuestion",
                "managed": True,
            },
        ),
        migrations.CreateModel(
            name="MedicalCenter",
            fields=[
                (
                    "medical_center_id",
                    models.AutoField(primary_key=True, serialize=False),
                ),
                ("email", models.EmailField(max_length=254)),
                ("telephone", models.CharField(max_length=14)),
            ],
        ),
        migrations.CreateModel(
            name="Symptom",
            fields=[
                ("symptom_id", models.AutoField(primary_key=True, serialize=False)),
                ("name", models.CharField(max_length=1000)),
            ],
            options={
                "db_table": "symptom",
                "managed": True,
            },
        ),
        migrations.DeleteModel(
            name="Prediction",
        ),
        migrations.AddField(
            model_name="diseasehassymptom",
            name="disease",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="triage.symptom"
            ),
        ),
        migrations.AddField(
            model_name="diseasehassymptom",
            name="symptom",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="triage.disease"
            ),
        ),
    ]
