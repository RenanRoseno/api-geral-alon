from django.http import Http404
from rest_framework import status, generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView

from api.models.campus import Campus
from api.serializers.campusSerializer import *


class SnippetDetail(APIView):
    """
    Retrieve, update or delete a snippet instance.
    """

    def get_object(self, pk):
        try:
            return Campus.objects.get(pk=pk)
        except Campus.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = CampusSerializer(snippet)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = CampusSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
