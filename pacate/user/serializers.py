from dataclasses import field

from rest_framework import serializers
from .models import User
from caresheet.serializer import CaresheetSerializer

class UserSerializer(serializers.ModelSerializer):
    # caresheet_all = CaresheetSerializer()
    class Meta:
        model = User
        fields = ["username", "password", "email"]