from api.models.campus import *
from api.serializers.campusSerializer import *
from django.shortcuts import get_object_or_404
from rest_framework import status, viewsets
from rest_framework.response import Response
from rest_framework.views import APIView


class CampusViewSet(APIView):
    # serializer_class = CampusSerializer
    #queryset = Campus.objects.all()
    print('campus view set')
    def get(self, request, id=None):
        if id:
            campus = Campus.objects.get(id=id)
            serializer = CampusSerializer(campus)
            return Response({"status": "sucess", "data": serializer.data}, status=status.HTTP_200_OK)
    
        elif id==None:
            campus = Campus.objects.all()
            serializer = CampusSerializer(campus, many=True)
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
        
    def post(self, request):
        print('def post acionado.')
        serializer = CampusSerializer(data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, id=None):
        print('def put acionado.')
        if id==None:
            return Response({"status": "error"}, status=status.HTTP_400_BAD_REQUEST)
        
        campus = get_object_or_404(Campus, id=id)      
        serializer = CampusSerializer(campus, data=request.data, partial=True)
        
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data})
        else:
            return Response({"status": "error", "data": serializer.errors})
