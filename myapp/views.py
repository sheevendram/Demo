from http.client import responses
from django.shortcuts import render

from rest_framework import generics

from myapp import models 

from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import MySerializer
from myapp import serializers

class ListToDo(generics.ListCreateAPIView):
    queryset = models.ToDo.objects.all()
    serializer_class = MySerializer

class ToDoCreateView(APIView):
    serializer_class = MySerializer

    def post(self, request):
        ser =MySerializer(data =request.data)
        if ser .is_valid():
            ser.save()
            return Responses(data =ser.data)
class ToDoDeleteView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class =MySerializer
    queryset = models.ToDo.objects.all()