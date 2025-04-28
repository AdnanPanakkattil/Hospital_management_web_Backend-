from rest_framework import serializers
from .models import *
# serializers.py

class DoctorsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctors
        fields ='__all__'


class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model= Department
        fields = '__all__'

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model=Contact
        fields = '__all__'

class AppoinmentSerializer(serializers.ModelSerializer):
    class Meta:
        model= Appoinment
        fields = '__all__'