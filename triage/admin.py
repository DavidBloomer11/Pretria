from django.contrib import admin
from .models import Encounter, Disease, Consultation, EncounterQuestion, EncounterDiseasePrediction, OpenAIModelConfiguration, Patient

# Register your models here.
admin.site.register(Encounter)
admin.site.register(Consultation)
admin.site.register(EncounterQuestion)
admin.site.register(Disease)
admin.site.register(EncounterDiseasePrediction)
admin.site.register(OpenAIModelConfiguration)
admin.site.register(Patient)