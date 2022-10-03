from dataclasses import field
from pyexpat import model
from rest_framework import serializers
from myapp import models

class MySerializer(serializers.ModelSerializer):
    class Meta:
        fields='__all__'
        model= models.ToDo