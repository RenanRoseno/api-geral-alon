from api.serializers.citySerializer import CitySerializer
from api.models.city import *
from rest_framework.viewsets import ReadOnlyModelViewSet, mixins, generics
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from django.http import Http404

class CitiesViewSet(ReadOnlyModelViewSet):

    queryset = City.objects.all()
    serializer_class = CitySerializer
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ['id_state', 'name']

    def get_queryset(self):
        name = self.request.query_params.get('name')
        queryset = City.objects.all()
        if name:
            queryset = queryset.filter(name__contains=name.upper())
            if not queryset:
                raise Http404
        return queryset
