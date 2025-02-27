# Generated by Django 4.1.7 on 2023-02-26 22:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Prediction",
            fields=[
                ("timestamp", models.DateTimeField(auto_created=True, auto_now=True)),
                ("prediction_id", models.AutoField(primary_key=True, serialize=False)),
                ("query", models.CharField(max_length=1000)),
                ("urgency_prediction", models.CharField(max_length=100)),
                ("urgency_prediction_certainty", models.FloatField()),
            ],
        ),
    ]
