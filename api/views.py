from django.http import JsonResponse
import time
from . serializers import EncounterSerializer, EncounterQuestionSerializer, ConsultationSerializer
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from triage.models import Encounter, EncounterQuestion
from .controller import EncounterController
from dashboard.controller import ConsultationController
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import action

# Create your views here.

@api_view(['POST','GET'])
def generate_encounter_questions(request, uuid):
    try:
        controller = EncounterController(uuid)
        question_list = controller.generate_questions()
        return Response(question_list)
    except Exception as e:
        print(e)
        
        return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST','GET'])
def generate_triage(request, uuid):
    
    controller = EncounterController(uuid)
    triage = controller.generate_triage()
    return Response(triage)
    

@api_view(['POST','GET'])
def generate_differential_diagnosis(request, uuid):
    try:
        controller = EncounterController(uuid)
        differential_diagnosis = controller.generate_differential_diagnosis()
        return Response(differential_diagnosis)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST','GET'])
def register_consultation(request):
    try:
        # Get UUID from follow up code
        follow_up_code = request.GET.get('follow_up_code')
        medical_practice_id = int(request.GET.get('medical_practice'))
        citizen_service_number = request.GET.get('citizen_service_number')

        controller = ConsultationController()
        consultation = controller.register_consultation(follow_up_code, citizen_service_number, medical_practice_id)
        serializer = ConsultationSerializer(consultation)
        
        return Response(serializer.data)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST','GET'])
def register_patient(request,uuid):
    '''Endpoint that takes an encounter and registers the patient for the encounter based on the citizen-service-number'''
    try:
        citizen_service_number = request.GET['citizen_service_number']

        controller = EncounterController(uuid=uuid)
        encounter = controller.register_patient(citizen_service_number)

        serializer = EncounterSerializer(encounter)
        
        return Response(serializer.data)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)




# Encounter API
class EncounterQuestionViewSet(viewsets.ModelViewSet):
    serializer_class = EncounterQuestionSerializer
    lookup_field = 'encounter_question_id'

    def get_queryset(self):
        # Only return questions that belong to the encounter
        return EncounterQuestion.objects.filter(encounter__uuid=self.kwargs['uuid'])

    @action(detail=True)
    def questions(self, request, uuid=None):
        # Use the nested viewset to handle the questions endpoint
        instance = self.get_object()
        queryset = self.get_queryset()
        serializer = EncounterQuestionSerializer(queryset, many=True)
        return Response(serializer.data)

class EncounterViewSet(viewsets.ModelViewSet):
    queryset = Encounter.objects.all()
    serializer_class = EncounterSerializer
    lookup_field = 'uuid'
