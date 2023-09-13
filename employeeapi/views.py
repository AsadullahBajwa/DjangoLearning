from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import EmployeeSerializer
from .models import Employee
# Create your views here.


@api_view(['GET'])
def employeeList(request):
    emps = Employee.objects.all().order_by('id')
    serializer = EmployeeSerializer(emps,many=True)
    return Response(serializer.data)

@api_view(['GET'])
def empDetails(request,pk):
    emp = Employee.objects.get(id=pk)
    serializer = EmployeeSerializer(emp,many=False)
    return Response(serializer.data)

@api_view(['POST'])
def empCreate(request):
    serializer = EmployeeSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
    
    return Response(serializer.data)

@api_view(['POST'])
def empUpdate(request,pk):
    emp = Employee.objects.get(id=pk)
    serializer = EmployeeSerializer(instance=emp,data =request.data)

    if serializer.is_valid():
        serializer.save()
    
    return Response(serializer.data)

@api_view(['DELETE'])
def empDelete(request,pk):
    emp = Employee.objects.get(id=pk)
    emp.delete()

    return Response('Item Deleted Successfully!')


@api_view(['PATCH'])
def empUpdate(request,pk):
    