from rest_framework import serializers
from triage.models import Encounter, EncounterQuestion, Consultation, OpenAIModelConfiguration

class EncounterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Encounter
        fields = '__all__'

    def create(self, validated_data):
        instance = super().create(validated_data)
        return {'uuid': instance.uuid}
    
class EncounterQuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = EncounterQuestion
        fields = '__all__'
    
    
class ConsultationSerializer(serializers.ModelSerializer):
    encounter = serializers.SlugRelatedField(
        slug_field='uuid',
        queryset=Encounter.objects.all()
    )
    class Meta:
        model = Consultation
        fields = '__all__'


class OpenAIModelConfigurationSerializer(serializers.ModelSerializer):
    class Meta:
        model = OpenAIModelConfiguration
        fields = '__all__'