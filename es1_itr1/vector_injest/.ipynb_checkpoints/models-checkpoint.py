from django.db import models

# Create your models here.

class DatabaseUnit(models.Model):
    database_unit_name = models.CharField(max_length=300)
    database_unit_description = models.TextField()
    date_added = models.DateTimeField("date added")
    
    def __str__(self):
        return self.database_unit_name

class ContentUnit(models.Model):
    database_unit = models.ForeignKey(DatabaseUnit, on_delete=models.CASCADE)
    
    content_unit_name = models.CharField(max_length=300)
    content_unit_description = models.TextField()
    date_added = models.DateTimeField("date added")
    
    def __str__(self):
        return self.content_unit_name

class ChunkUnit(model.Model):
    content_unit = models.ForeignKey(ContentUnit, on_delete=models.CASCADE)
    
    chunk_unit_name = models.CharField(max_length=300)
    chunk_unit_reference = ""
    date_added = models.DateTimeField("date added")
    
    def __str__(self):
        return self.chunk_unit_name