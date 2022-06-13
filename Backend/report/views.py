from rest_framework import generics
from .models import Report
from .serializers import ReportSerializer
# Create your views here.

class index(generics.ListAPIView):
    queryset = Report.objects.all()
    serializer_class = ReportSerializer
