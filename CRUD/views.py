from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from .serializers import DatasetSerializers
from .models import DataSet


# Create your views here.
class DatasetInsertView(generics.ListCreateAPIView):
    serializer_class = DatasetSerializers
    queryset = DataSet.objects.all()


class IndexviewSet(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = DatasetSerializers
    queryset = DataSet.objects.all()
