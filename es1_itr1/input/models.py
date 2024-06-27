from django.db import models

# Create your models here.

class DatasetUnit(models.Model):
    dataset_unit_name = models.CharField(max_length=300)
    dataset_unit_description = models.TextField()
    date_added = models.DateTimeField("date added")
    content_path = models.CharField(max_length=500)
    directory_structure = models.TextField()
    
    def __str__(self):
        return self.dataset_unit_name