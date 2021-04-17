from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView

from personalInfo import models
from . import serializers
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
#from django.http import HttpResponse
from rest_framework import status
from django.shortcuts import render
from rest_framework.renderers import HTMLFormRenderer, JSONRenderer, BrowsableAPIRenderer

class PersonalInfoList(APIView):
    permission_classes = [IsAuthenticated,]

    serializer_class = serializers.PersonalInfoSerializer
    renderer_classes = (BrowsableAPIRenderer, JSONRenderer, HTMLFormRenderer)

    def get(self, request):
        if request.user.is_authenticated:
            #do something
            queryset = models.PersonalInfo.objects.filter(User_id=request.user.id)
            serializer = serializers.PersonalInfoSerializer(queryset, many=True)
            return Response(serializer.data)

    def post(self, request, format=None):
        serializer = serializers.PersonalInfoSerializer(data = request.data)         
        
        if serializer.is_valid():
            serializer.save(user= request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)