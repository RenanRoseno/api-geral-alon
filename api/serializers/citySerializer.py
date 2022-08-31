from rest_framework import serializers
from api.models import city


class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = city.City
        fields = "__all__"
