from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class MedicalPractice(models.Model):
    medical_practice_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)


class Doctor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    
class DoctorAtMedicalPractice(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete= models.CASCADE)
    medical_practice = models.ForeignKey(MedicalPractice, on_delete= models.CASCADE)

    class Meta:
        unique_together = (('doctor','medical_practice'))

