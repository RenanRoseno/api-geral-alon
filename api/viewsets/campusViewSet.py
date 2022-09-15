from json import JSONEncoder

from api.models.campus import *
from api.models.city import *
from api.serializers.campusSerializer import *
from django.http import Http404
from rest_framework import status, viewsets
from rest_framework.response import Response
from rest_framework.views import APIView


class CampusViewSet(APIView):

    def get(self, request, id=None):
        if id:
            try: 
                campus = Campus.objects.get(id=id)
            except Campus.DoesNotExist:
                return Response({"status":"A campus with this id does not exist."}, status=status.HTTP_404_NOT_FOUND)
            
            serializer = CampusSerializer(campus)
            return Response({"status": "sucess", "data": serializer.data}, status=status.HTTP_200_OK)
    
        elif id==None:
            campus = Campus.objects.all()
            serializer = CampusSerializer(campus, many=True)
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
        
    def post(self, request):
        serializer = CampusSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({"status": "invalid data", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, id=None):
        if id:
            try: 
                campus = Campus.objects.get(id=id)
            except Campus.DoesNotExist:
                return Response({"status":"A campus with this id does not exist."}, status=status.HTTP_404_NOT_FOUND)
        elif id==None:
            return Response({"status": "A campus id is required."}, status=status.HTTP_400_BAD_REQUEST)
        
        serializer = CampusSerializer(campus, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data})
        else:
            return Response({"status": "Error. The body data is invalid", "data": serializer.errors})
        
    def delete(request, id=None):
        if id:
            try: 
                campus = Campus.objects.get(id=id)
            except Campus.DoesNotExist:
                return Response({"status":"A campus with this id does not exist."}, status=status.HTTP_404_NOT_FOUND)
        elif id==None:
            return Response({"status": "Error. A delete method needs a id."}, status=status.HTTP_400_BAD_REQUEST)
        campus.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class CampusQuerySet(viewsets.ModelViewSet):
    serializer_class = CampusSerializer

    def get_queryset(self):
        id_city = self.request.query_params.get('id_city')
        id_state = self.request.query_params.get('id_state')
        
        if id_city==None and id_state==None:
            return Response({"status":"A queryset must have a parameter."})
        
        elif id_city and id_state==None:
            campus= Campus.objects.filter(id_city=id_city)
            
        elif id_city==None and id_state:

            campus = Campus.objects.raw(f"SELECT * FROM campus c inner join cities cit on cit.id = c.id_city inner join states s on s.id = cit.id_state Where  s.id = {id_state}")
            cities = City.objects.filter(id_state=id_state)
            for city in cities:
                print(f'{city} {city.id}')
            return campus       
        
        if campus: 
            campus= Campus.objects.filter(id_city=id_city)
            return campus #Response({"status": "sucess", "data": serializer.data}, status=status.HTTP_200_OK)
        elif not campus:
            raise Http404 

