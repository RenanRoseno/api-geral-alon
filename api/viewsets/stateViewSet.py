from api.models.state import *
from api.serializers.stateSerializer import *
from django.http import Http404
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.views import APIView


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
    
'''
class StateView(APIView):
    def get(self, request, name=None):
        if name:
            name = name.upper()
            state = State.objects.get(name=name)
            serializer = StateSerializer(state)
            return Response({"status": "sucess", "data": serializer.data}, status=status.HTTP_200_OK)
    
        elif name==None:
            state = State.objects.all()
            serializer = StateSerializer(state, many=True)
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
        
    def get_queryset(self):
        queryset = State.objects.all()
        abbreviation = self.request.query_params.get('abbreviation')
        
        if abbreviation:
            queryset = queryset.filter(name__contains=abbreviation.upper())
            if not queryset:
                raise Http404
        return queryset
'''
