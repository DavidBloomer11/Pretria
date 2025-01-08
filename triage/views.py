from django.shortcuts import render, redirect
from utils.openai_connector import OpenAiChatConnector
import json
from .models import Consultation, Encounter, EncounterQuestion
from . import controller

# Create your views here.

def home(request):
    return render(request,'index.html')

'''
Depreciated code...


def primary_symptom_query(request):
    if request.method == 'POST':
        #Check if there is a description of the symptoms
        age = request.POST.get('age')
        query = request.POST.get('query')
        gender = request.POST.get('gender')

        response = controller.primary_symptom_controller(age,query, gender)

        if response == False:
            return render(request,'primary_symptom_query.html',{'error':True})
        else:
            #Create new session
            request.session['uuid'] = str(response)

            return redirect('questionnaire')
    
    else:
        return render(request,'primary_symptom_query.html')


def questionnaire(request):
    #Redirect if session doesn't exist yet
    if 'uuid' not in request.session:
        return redirect('primary_symptom_query')

    #Get encounter via uuid in session
    uuid = request.session.get('uuid')
    encounter = Encounter.objects.get(uuid=uuid)
    question_list = EncounterQuestion.objects.filter(encounter=encounter)
    
    if request.method == 'POST':
        pass
    else:
        context = {
            'question_list' : question_list
        }

        return render(request,'questionnaire.html',context)

    if request.method == 'POST':
        #Retrieve and save answers
        for question in question_list:
            answer = request.POST.get(str(question.pk))
            question.answer = answer
            question.save()
        return redirect(triage_prediction)
            

def triage_prediction(request):
    #Redirect if session doesn't exist yet
    if 'uuid' not in request.session:
        return redirect('primary_symptom_query')
    else:
        encounter = Encounter.objects.get(uuid=request.session.get('uuid'))

        response = controller.triage_prediction_controller(encounter)
        
    
    context = {
        'encounter' : encounter
    }

    return render(request,'triage_prediction.html',context)


def register(request):
    if request.method == 'POST':
        medical_practice = 1
        code = request.POST.get('code')

        success, message = Encounter.register_follow_up(code, medical_practice)
        context = {
            'success' : success,
            'message' : message
        }    

        return render(request,'register.html', context)
    else:
        return render(request,'register.html')
'''
