from django.urls import path, include
from . import views

urlpatterns = [
    path('<int:id>/',views.dashboard,name='dashboard'),
    path('login/',views.login_view,name='login'),
    path('logout/',views.logout_view,name='logout'),
    path('select-medical-practice/',views.select_medical_practice,name='select_medical_practice'),
    path('<int:id>/consultations/',views.consultations,name='consultations'),
    path('<int:id>/consultations/<int:consultation_id>/',views.consultation,name='consultation'),
    path('<int:id>/register-consultation/',views.register_consultation,name='register-consultation'),
    path('<int:id>/consultations/<int:consultation_id>/perform/',views.perform_consultation, name='perform_consultation')
]
