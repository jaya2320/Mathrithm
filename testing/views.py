from django.shortcuts import render
from .serializer import *
from rest_framework.views import APIView
from rest_framework.response import Response
import json
# Create your views here.
class users(APIView):
    serializer_class=AllUser
    def get(self,request):

        ser=AllUser(User.objects.all(),context={'request': request, },many=True)
        return Response({'users':ser.data})

class user_info(APIView):
    def get(self,request,user_id):
        
        ser=particularuser(User.objects.get(id=user_id),context={'request': request})
        return Response({
            'user': ser.data,
        }
               
                )
