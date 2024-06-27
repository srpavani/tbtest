from rest_framework.viewsets import ModelViewSet
from .models import Territorio, Quadra
from .serializers import TerritorioSerializer, QuadraSerializer
from rest_framework.permissions import AllowAny

class TerritorioViewSet(ModelViewSet):  # testando o bulk create 
    queryset = Territorio.objects.all()
    serializer_class = TerritorioSerializer
    permission_classes = [AllowAny]
    
    
class QuadraViewSet(ModelViewSet):  # testando o bulk create 
    queryset = Quadra.objects.all()
    serializer_class = QuadraSerializer
    permission_classes = [AllowAny]    
