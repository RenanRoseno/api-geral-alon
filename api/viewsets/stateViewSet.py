from rest_framework import viewsets
from api.serializers.stateSerializer import *
from api.models.state import *


class StateViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = StateSerializer
    queryset = State.objects.all()
