from tkinter import CASCADE
from turtle import ondrag
from typing import ValuesView
from django.db import models
from pacate.caresheet.manager import CaresheetManager, WeightRecordManager
from user.models import User

# Create your models here.

class Caresheet(models.Model):

    objects: CaresheetManager = CaresheetManager()

    master = models.ForeignKey(User, on_delete= models.CASCADE, related_name= 'Master')
    name = models.CharField("이름", max_length=20, unique= True)
    sex = models.CharField("성별", max_length=20, choices=[("F","Female"), ("M", "Male")])
    morph = models.CharField("모프", max_length=20)
    regist_date = models.DateTimeField("등록일", auto_now_add= True)

    def __str__(self):
        return f'Master :{self.master}, {self.name} , {self.morph}, sex:{self.sex}'
    
    def change_name(self,rookie):
        self.update(name= rookie)
    
    def testtest(self):
        self.update(weight= 40)


# #manage.py

# def abc(self):
#     return self.get(user=fdsjakllfd)

# def weight_test(self):
#     return self.filter(weight__gte = 10) # 10이상의 개체가 쿼리셋으로 반환

# view
# test = Caresheet.objects.abc
# # 쿼리셋이니까
# test.change_name('ababa')

# view

# testest = Caresheet.objects.weight_test()
# #10이상인것만 쿼리셋으로 나옴

# for i in testest:
#     i.testtset()
#     #전부 testtest() 를 받아서 40으로 변경


class WeightRecord(models.Model):

    objects: WeightRecordManager = WeightRecordManager()

    name = models.ForeignKey(Caresheet, on_delete= models.CASCADE, related_name= "개체명")
    weight = models.FloatField("무게")
    record_date = models.DateField("기록일", auto_now_add= True)

    def __str__(self):
        return f'{self.name} 의 {self.record_date} 무게 : {self.weight}'
    
    def get_past_weight_record(self):
        weight_list = WeightRecord.objects.get_weight_records()
        return weight_list