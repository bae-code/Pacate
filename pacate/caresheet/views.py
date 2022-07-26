from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import permissions, status

from caresheet.serializer import CaresheetSerializer
from caresheet.models import Caresheet,WeightRecord

# Create your views here.
class CaresheetView(APIView): # CBV 방식
    permission_classes = [permissions.AllowAny] # 누구나 view 조회 가능
    # permission_classes = [permissions.IsAdminUser] # admin만 view 조회 가능
    # permission_classes = [permissions.IsAuthenticated] # 로그인 된 사용자만 view 조회 가능

    # load all caresheets user have

    def get(self, request):
        user = request.user.id
        user_sheets = Caresheet.objects.filter(master_id=user)
        serialized_care_data = CaresheetSerializer(user_sheets, many=True).data
        print(serialized_care_data[0]['name'])
        return Response(serialized_care_data, status = status.HTTP_200_OK)
        
    def post(self, request):
        return Response({'message': 'post method!!'})

    def put(self, request):
        return Response({'message': 'put method!!'})

    def delete(self, request):
        return Response({'message': 'delete method!!'})



# Caresheet Detail
class CaresheetDetailView(APIView):

    def get(self, request):

        #Find Caresheet
        
        #Click Caresheet name func got name in caresheet page
        caresheet = Caresheet.objects.filter(name="F2")[0]
        name, sex, morph, regist_date = caresheet.name, caresheet.sex, caresheet.morph, caresheet.regist_date.date()

        #Find Weight Record 
        
        # Need caresheet of name_id 
        recent_sort = WeightRecord.objects.filter(name_id=1).order_by('record_date')
        past_sort = WeightRecord.objects.filter(name_id=1).order_by('-record_date')
        present_weight = recent_sort[0].weight
        all_weight_records = []
        for _ in past_sort:
            all_weight_records.append(_.weight)
        
        caresheet_information = {"name": name,"sex": sex, "morph": morph, "regist_date": regist_date,"present_weight" :present_weight,"all_weight" :all_weight_records}
        return Response(caresheet_information, status = status.HTTP_200_OK)
        