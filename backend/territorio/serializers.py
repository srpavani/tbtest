from rest_framework.serializers import ModelSerializer
from .models import Territorio, Quadra


class TerritorioSerializer(ModelSerializer):
    
    class Meta:
        model = Territorio
        fields = '__all__'


class QuadraSerializer(ModelSerializer):
    
    class Meta:
        model = Quadra
        fields = '__all__'

