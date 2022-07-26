from tkinter import CASCADE
from turtle import ondrag
from django.db import models
from user.models import User

# Create your models here.

class Caresheet(models.Model):
    master = models.ForeignKey(User, on_delete= models.CASCADE, related_name= 'Master')
    name = models.CharField("이름", max_length=20, unique= True)
    sex = models.CharField("성별", max_length=20, choices=[("F","Female"), ("M", "Male")])
    morph = models.CharField("모프", max_length=20)
    regist_date = models.DateTimeField("등록일", auto_now_add= True)

    def __str__(self):
        return f'Master :{self.master}, {self.name} , {self.morph}, sex:{self.sex}'

class WeightRecord(models.Model):
    name = models.ForeignKey(Caresheet, on_delete= models.CASCADE, related_name= "개체명")
    weight = models.FloatField("무게")
    record_date = models.DateField("기록일", auto_now_add= True)

    def __str__(self):
        return f'{self.name} 의 {self.record_date} 무게 : {self.weight}'