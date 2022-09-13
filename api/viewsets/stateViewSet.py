from api.models.state import *
from api.serializers.stateSerializer import *
from django.http import Http404
from rest_framework import viewsets


class StateViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = StateSerializer
    queryset = State.objects.all()

    def get_queryset(self):
        queryset = State.objects.all()
        abbreviation = self.request.query_params.get('abbreviation')
        
        if abbreviation:
            queryset = queryset.filter(name__contains=abbreviation.upper())
            if not queryset:
                raise Http404
        return queryset
