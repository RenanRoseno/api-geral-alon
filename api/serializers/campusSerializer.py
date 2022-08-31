from rest_framework import serializers
from api.models import campus


class CampusSerializer(serializers.ModelSerializer):
    class Meta:
        model = campus.Campus
        fields = "__all__"
