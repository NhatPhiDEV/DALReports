from django.db import models
from report.models import Report
from category.models import Category

# Create your models here.

class SalesReport(models.Model):
    """
    Sales Report Model
    """
    date = models.DateField()
    total = models.DecimalField(max_digits=10, decimal_places=2)
    unit = models.CharField(max_length=5)
    report = models.ForeignKey(Report, on_delete=models.CASCADE, related_name='reports')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='categories')
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'sales_report'
        ordering = ['-id']