from atexit import register
from calendar import WEDNESDAY
from django.contrib import admin
from .models import Caresheet,WeightRecord
# Register your models here.

admin.site.register(Caresheet)
admin.site.register(WeightRecord)