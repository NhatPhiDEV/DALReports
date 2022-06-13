'''
    class SalesReportSerializer
'''
from rest_framework import serializers
from .models import SalesReport


class SalesReportSerializer(serializers.ModelSerializer):
    report_name = serializers.SerializerMethodField('get_report_name')
    category_name = serializers.SerializerMethodField('get_category_name')

    class Meta:
        model = SalesReport
        fields = ['id', 'date', 'total', 'unit', 'report_name', 'category_name', 'created_at', 'modified_at']
        read_only_fields = ['created_at', 'modified_at']

    def get_report_name(self, obj):
        return obj.report.name

    def get_category_name(self, obj):
        return obj.category.name