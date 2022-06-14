from rest_framework import generics
from .models import SalesReport
from .serializers import SalesReportSerializer
# Create your views here.

class index(generics.ListAPIView):
    queryset = SalesReport.objects.all()
    serializer_class = SalesReportSerializer

    # def get_queryset(self):
    #     queryset = SalesReport.objects.all()
    #     start_date = self.request.query_params.get('start_date', None)
    #     end_date = self.request.query_params.get('end_date', None)
    #     if start_date is not None and end_date is not None:
    #         queryset = queryset.filter(date__range=(start_date, end_date))
    #     return queryset