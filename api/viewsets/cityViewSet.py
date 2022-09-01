from rest_framework import viewsets
from api.serializers.citySerializer import CitySerializer
from api.models.city import *


class CityViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = CitySerializer
    queryset = City.objects.all()
