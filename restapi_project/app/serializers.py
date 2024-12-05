from rest_framework import serializers
from .models import *

class Sample(serializers.Serializer):
    roll_no=serializers.IntegerField()
    name=serializers.CharField()
    age=serializers.IntegerField()
    email=serializers.EmailField()

class Model_serializer(serializers.ModelSeraializer):
    class Meta:
        model=Project
        fields='__all__'