# Generated by Django 4.1.7 on 2023-04-14 22:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        (
            "dashboard",
            "0002_rename_doctoratmedicalcenter_doctoratmedicapractice_and_more",
        ),
    ]

    operations = [
        migrations.RenameModel(
            old_name="DoctorAtMedicaPractice",
            new_name="DoctorAtMedicalPractice",
        ),
    ]
