from collections import UserList
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import permissions, status
from django.contrib.auth import login, authenticate

from user.serializers import UserSerializer


# Create your views here.
class UserView(APIView): # CBV 방식
    permission_classes = [permissions.AllowAny] # 누구나 view 조회 가능
    # permission_classes = [permissions.IsAdminUser] # admin만 view 조회 가능
    # permission_classes = [permissions.IsAuthenticated] # 로그인 된 사용자만 view 조회 가능

    def get(self, request):
        user = request.user
        serialized_user_data = UserSerializer(user).data
        username = serialized_user_data['username']
        welcome_comment = f'환영합니다 ! {username}'
        return Response(welcome_comment, status = status.HTTP_200_OK)
        
    def post(self, request):
        username = request.data.get('username' , '')
        password = request.data.get('password' , '')

        user = authenticate(request, username=username, password=password)
        print(username,password)
        if not user:
            return Response({"error": "존재하지않는 계정 이거나 비밀번호 오류"})
        login(request, user)
        return Response({"message":"로그인"}, status=status.HTTP_200_OK)
    def put(self, request):
        return Response({'message': 'put method!!'})

    def delete(self, request):
        return Response({'message': 'delete method!!'})