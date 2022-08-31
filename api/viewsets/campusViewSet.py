from rest_framework import viewsets
from api.serializers.campusSerializer import *
from api.models.campus import *


class CampusViewSet(viewsets.ModelViewSet):
    serializer_class = CampusSerializer
    queryset = Campus.objects.all()
