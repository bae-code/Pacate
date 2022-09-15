from django.db import models

class CaresheetManager(models.Manager):

    def my_caresheets(self,user):
        return self.filter(master_id=user)

    def weight_test(self):
        return self.filter(weight__gte = 10)

class WeightRecordManager(models.Manager):

    def get_weight_records(self,id):
        return self.filter(name_id=id).order_by('record_date').values_list("weight")
