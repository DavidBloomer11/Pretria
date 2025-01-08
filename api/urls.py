from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'encounters', views.EncounterViewSet)
router.register(r'encounters/(?P<uuid>[^/.]+)/questions', views.EncounterQuestionViewSet, basename='encounter-question')

urlpatterns = [
    path('', include(router.urls)),
    path('encounters/<str:uuid>/generate_questions/', views.generate_encounter_questions),
    path('encounters/<str:uuid>/generate_triage/', views.generate_triage),
    path('encounters/<str:uuid>/generate_differential_diagnosis/', views.generate_differential_diagnosis),
    path('encounters/<str:uuid>/register_patient/', views.register_patient),

    #Consultations
    path('consultations/register/',views.register_consultation),

]
