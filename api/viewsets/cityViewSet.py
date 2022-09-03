from rest_framework import viewsets
from api.serializers.citySerializer import CitySerializer
from api.models.city import *


class CityViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = CitySerializer
    queryset = City.objects.all()

    def get_queryset(self):
        queryset = City.objects.all()
        name = self.request.query_params.get('idState')
        if name:
            queryset = queryset.filter(name__contains=name.upper())
        return queryset
