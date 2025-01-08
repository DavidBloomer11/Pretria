from django.contrib import admin
from . import models
from django.contrib.auth.models import Permission
# Register your models here.
admin.site.register(models.Doctor)
admin.site.register(models.MedicalPractice)
admin.site.register(models.DoctorAtMedicalPractice)
admin.site.register(Permission)