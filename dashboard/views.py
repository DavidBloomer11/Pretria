from django.shortcuts import render, get_object_or_404
from triage.models import Encounter, Consultation, EncounterQuestion, EncounterDiseasePrediction, Disease
from .models import MedicalPractice, Doctor, DoctorAtMedicalPractice
from functools import wraps
from django.contrib.auth.decorators import login_required
from .controller import ConsultationController
from datetime import datetime, date
import asyncio
from api.controller import EncounterController
from asgiref.sync import sync_to_async

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout

def doctor_linked_to_medical_practice(view_func):
    '''Checks if doctor is linked to a medical center to gain access to its files'''
    @wraps(view_func)
    def wrapper(request, *args, **kwargs):
        pk = kwargs.get('id')
        medical_practice = get_object_or_404(MedicalPractice, pk=pk)
        try:
            doctor_at_practice = DoctorAtMedicalPractice.objects.get(doctor=request.user.doctor, medical_practice=medical_practice)
        except AttributeError:
            #User isn't a doctor
            return redirect('/dashboard/login/')
        except DoctorAtMedicalPractice.DoesNotExist:
            #Error if doctor isn't assigned to medical practice. User should know why he is being redirected
            return redirect('/dashboard/login/',error='1')
        return view_func(request, *args, **kwargs)
    return wrapper


@doctor_linked_to_medical_practice
def dashboard(request,id):
    medical_practice = get_object_or_404(MedicalPractice, pk=id)

    context = {
        'medical_practice' : medical_practice,
        'number_of_consultations_today' : Consultation.get_number_of_consultations(id, date_start=date.today(), date_end=date.today()),
        'number_in_waiting_room' : Consultation.get_number_in_waiting_room(id),
        'waiting_room_list' : Consultation.get_waiting_room(id),
        'average_consultation_time' : Consultation.get_average_consultation_time()
    }

    return render(request,'dashboard_home.html',context)


@doctor_linked_to_medical_practice
def consultations(request,id):
    medical_practice = get_object_or_404(MedicalPractice, pk=id)

    consultation_list = Consultation.objects.filter(medical_practice=medical_practice)


    context = {
        'medical_practice':medical_practice,
        'consultation_list' : consultation_list
    }
    return render(request,'consultations.html',context)

@doctor_linked_to_medical_practice
def consultation(request,id,consultation_id):
    medical_practice = get_object_or_404(MedicalPractice, pk=id)
    consultation = get_object_or_404(Consultation,pk=consultation_id)

    disease_prediction_list = EncounterDiseasePrediction.objects.filter(encounter = consultation.encounter)
    question_list = EncounterQuestion.objects.filter(encounter = consultation.encounter)

    context = {
        'medical_practice':medical_practice,
        'consultation' : consultation,
        'disease_prediction_list' : disease_prediction_list,
        'question_list' : question_list
    }
    
    return render(request, 'consultation.html',context)


def login_view(request):
    if request.method == 'POST':
        user = authenticate(username=request.POST['username'], password=request.POST['password'])
        if user is not None:
            #Login user
            login(request, user)
            #Redirect to dashboard that user has access to
            return redirect('select_medical_practice')
        else:
            return render(request, 'login.html',context={'error':'Enter a correct username or password.'})
    else:
        return render(request, 'login.html')
    
@login_required(login_url='/dashboard/login/')
def select_medical_practice(request):
    if request.method == 'POST':
        id = request.POST.get('medical_practice')
        return redirect('dashboard',id=id)
    else:
        context = {
            'medical_practice_list' : DoctorAtMedicalPractice.objects.filter(doctor=Doctor.objects.get(user = request.user))
        }

        return render(request,'select_medical_practice.html',context=context)


def logout_view(request):
    if request.session:
        logout(request)
        return redirect('login')
    else:
        return redirect('login')
    

def register_consultation(request,id):
    if request.method == 'POST':
        try:
            follow_up_code = request.POST.get('follow_up_code')
            citizen_service_number = request.POST.get('citizen_service_number')

            controller = ConsultationController()
            consultation = controller.register_consultation(follow_up_code,citizen_service_number,id)

            #Now you can make differential diagnosis, but do this async
            controller = EncounterController(consultation.encounter.uuid)
            controller.generate_differential_diagnosis()
            

            message = f'Patient {consultation.encounter.patient.first_name} {consultation.encounter.patient.last_name} succesfully registered for a consultaion.'
            return render(request,'register_consultation.html',{'success':message})
        except Exception as e:
            return render(request,'register_consultation.html',{'error':e})
    else:
        return render(request,'register_consultation.html')
    

def perform_consultation(request,id,consultation_id):
    consultation = get_object_or_404(Consultation,pk=consultation_id)
    medical_practice = get_object_or_404(MedicalPractice, pk=id)
    if request.method == 'POST':
        controller = ConsultationController()
        controller.perform_consultation(request.POST,consultation)

        return redirect('consultation',id, consultation_id)

    else:
        disease_prediction_list = EncounterDiseasePrediction.objects.filter(encounter = consultation.encounter)
        question_list = EncounterQuestion.objects.filter(encounter = consultation.encounter)
        disease_list = Disease.objects.all()

        #Set consultation doctor & time
        consultation.doctor = Doctor.objects.get(pk=request.user.pk)
        consultation.datetime_start_consultation = datetime.now()
        consultation.save()

        context = {
            'medical_practice':medical_practice,
            'consultation' : consultation,
            'disease_prediction_list' : disease_prediction_list,
            'question_list' : question_list,
            'disease_list' : disease_list
        }

        return render(request, 'consultation_process.html',context)