from rest_framework import viewsets
from api.serializers.stateSerializer import *
from api.models.state import *


class StateViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = StateSerializer
    queryset = State.objects.all()

    def get_queryset(self):
        queryset = State.objects.all()
        name = self.request.query_params.get('name')
        if name:
            queryset = queryset.filter(name__contains=name.upper())
        return queryset
