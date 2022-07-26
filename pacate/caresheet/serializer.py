from dataclasses import field

from pkg_resources import require

from setuptools import Require
from rest_framework import serializers
from .models import Caresheet,WeightRecord

class WeightRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = WeightRecord
        fields = ["weight", "record_date"]

class CaresheetSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Caresheet
        fields = ["name", "morph", "sex"]