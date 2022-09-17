from api.serializers.citySerializer import CitySerializer
from api.models.city import *
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import Http404
from rest_framework import viewsets
from rest_framework import status
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from rest_framework import viewsets, filters
from django.shortcuts import get_object_or_404
from rest_framework.decorators import action


class CitiesViewSet(viewsets.ModelViewSet):

    queryset = City.objects.all()
    serializer_class = CitySerializer
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ['id_state', 'name']
    http_method_names = ['get', 'head']


    def retrieve(self, request, *args, **kwargs):
        name = self.get_object()
        if name is None:
            return Response({'detail': 'Not Found'}, status=404)
        return Response([CitySerializer(x).data for x in City.objects.filter(name=name)])
