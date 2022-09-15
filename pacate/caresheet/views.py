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
        user_sheets = Caresheet.objects.my_caresheets(request.user.id)
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
        #매니저로 이동#
        a = WeightRecord.get_past_weight_record(caresheet)
        #############
        ## mixin 으로 이동####

        #####################
        caresheet_information = {"name": name,"sex": sex, "morph": morph, "regist_date": regist_date,"present_weight" :a[-1],"all_weight" : a}
        return Response(caresheet_information, status = status.HTTP_200_OK)
        