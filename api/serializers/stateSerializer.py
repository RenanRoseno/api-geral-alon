from rest_framework import serializers
from api.models import state


class StateSerializer(serializers.ModelSerializer):
    class Meta:
        model = state.State
        fields = "__all__"
