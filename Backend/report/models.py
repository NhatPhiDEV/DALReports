from django.db import models

# Create your models here.

class Report(models.Model):
    """
    Report model
    """
    name = models.CharField(max_length=100)
    description = models.TextField()

    class Meta:
        db_table = 'report'

    def __str__(self):
        return self.name
        
