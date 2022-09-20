from api.models.campus import *
from api.serializers.campusSerializer import *
from rest_framework import generics, mixins, status, viewsets
from rest_framework.response import Response


class CampusViewSet(viewsets.ModelViewSet):
    serializer_class = CampusSerializer
    queryset = Campus.objects.all()

    def get_queryset(self):
        name = self.request.query_params.get('name')
        id_state = self.request.query_params.get('id_state')
        id_city = self.request.query_params.get('id_city')
        queryset = Campus.objects.all()
        
        if name:
            queryset = queryset.filter(name__contains=name.upper())
        if id_state:
            queryset = Campus.objects.raw(f"SELECT * FROM campus c inner join cities cit on cit.id = c.id_city inner join states s on s.id = cit.id_state Where  s.id = {id_state}")
        if id_city:
            queryset = queryset.filter(id_city=id_city)
        return queryset

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        if getattr(instance, '_prefetched_objects_cache', None):
            # If 'prefetch_related' has been applied to a queryset, we need to
            # forcibly invalidate the prefetch cache on the instance.
            instance._prefetched_objects_cache = {}

        return Response(serializer.data)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)
