from django.shortcuts import render
from rest_framework import generics
from .models import SalesReport
from .serializers import SalesReportSerializer

# Create your views here.

class index(generics.ListAPIView):
    queryset = SalesReport.objects.all()
    serializer_class = SalesReportSerializer
