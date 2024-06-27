from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewset import TerritorioViewSet, QuadraViewSet



router = DefaultRouter()
router.register(prefix='territorio', viewset = TerritorioViewSet, basename='teritorio')
router.register(prefix='territorio', viewset = TerritorioViewSet, basename='teritorio')


urlpatterns = [
    path('', include(router.urls)),
    path('territorio/', include('territorio.urls'))
]
