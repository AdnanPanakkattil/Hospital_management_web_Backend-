from django.shortcuts import render, redirect
from django.contrib import messages
from .models import *
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .serializer import *
from rest_framework.permissions import AllowAny

# Create your views here.
def index(request):
    return render(request, "index.html")

#..........Api..............
 
class DoctorsApi(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        data = Doctors.objects.all()
        serializer = DoctorsSerializer(data, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


    def post(self, request):
        serializer = DoctorsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.error_messages, status=status.HTTP_400_BAD_REQUEST)


    def put(self, request, id):
        try:
            data = Doctors.objects.get(id=id)
        except Doctors.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = DoctorsSerializer(data, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.error_messages, status=status.HTTP_400_BAD_REQUEST)


    def delete(self, request, id):
        try:
            data = Doctors.objects.get(id=id)
        except Doctors.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        data.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



class DepartmentApi(APIView):
    permission_classes = [AllowAny]
    def get(self, request):
        data = Department.objects.all()
        serializer = DepartmentSerializer(data, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        serializer = DepartmentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.error_messages, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, id):
        try:
            data = Department.objects.get(id=id)
        except Department.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = DepartmentSerializer(data, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.error_messages, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, id):
        try:
            data = Department.objects.get(id=id)
        except Department.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        data.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


     
class ContactApi(APIView):
     permission_classes=[AllowAny]
     def get(self,requast):
         data = Contact.objects.all()
         serializer = ContactSerializer(data,many=True)
         return Response(serializer.data,status=status.HTTP_200_OK)
     

     def post(self,request):
        serializer =ContactSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.error_messages,status=status.HTTP_400_BAD_REQUEST)
     
     
class AppoinmentApi(APIView):
    permission_classes=[AllowAny]
    def get(self,requast):
        data = Appoinment.objects.all()
        serializer = AppoinmentSerializer(data,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
    def post(self,request):
        serializer =AppoinmentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.error_messages,status=status.HTTP_400_BAD_REQUEST)
    
    