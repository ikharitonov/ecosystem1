from django.db import models

# Create your models here.

class StructureUnit(models.Model):
    
    # name
    # database_belongs_to
    # parent
    # children
    # is_top_node
    # is_end_node
    # type: Content or Folder
    # element_format: PDF File
    # path
    # run during html directory scanning function
    
    dataset_unit_name = models.CharField(max_length=300)
    dataset_unit_description = models.TextField()
    date_added = models.DateTimeField("date added")
    content_path = models.CharField(max_length=500)
    directory_structure = models.TextField()
    
    # children = 
    
    def __str__(self):
        return self.dataset_unit_name