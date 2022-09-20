from api.models.state import *
from api.serializers.stateSerializer import *
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from rest_framework.viewsets import ReadOnlyModelViewSet
from django.http import Http404


class StateViewSet(ReadOnlyModelViewSet):

    queryset = State.objects.all()
    serializer_class = StateSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ['abbreviation', 'name']
    http_method_names = ['get', 'head']


    def get_queryset(self):
        queryset = State.objects.all()
        abbreviation = self.request.query_params.get('abbreviation')
        name = self.request.query_params.get('name')

        if abbreviation:
            queryset = queryset.filter(name__contains=abbreviation.upper())
            if not queryset:
                raise Http404
        if name:
            queryset = queryset.filter(name__contains=name.upper())
            if not queryset:
                raise Http404
        return queryset
    