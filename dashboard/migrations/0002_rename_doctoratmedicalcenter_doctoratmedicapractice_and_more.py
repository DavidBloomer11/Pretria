# Generated by Django 4.1.7 on 2023-04-14 21:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("dashboard", "0001_initial"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="DoctorAtMedicalCenter",
            new_name="DoctorAtMedicaPractice",
        ),
        migrations.RenameModel(
            old_name="MedicalCenter",
            new_name="MedicalPractice",
        ),
    ]
