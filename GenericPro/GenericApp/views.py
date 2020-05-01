from django.shortcuts import render
from GenericApp.serializers import EmpSerializer
from rest_framework import generics
from GenericApp.models import Emp
class GenericView_List(generics.ListCreateAPIView):
    """ list: Return a list of all Employees. create: Create a new Employee. """
    queryset = Emp.objects.all()
    serializer_class = EmpSerializer
class GenericView_Details(generics.RetrieveUpdateDestroyAPIView):
    """ retrieve: Return the given Employee. destroy: Delete a Employee. update: Update a Employee. partial_update: Update a Employee. """
    queryset = Emp.objects.all()
    serializer_class = EmpSerializer
