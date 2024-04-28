from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.utils import timezone

import os
import zipfile

from .forms import DatasetForm
from .models import DatasetUnit

# Create your views here.

'''
TODO:
- handle creation of dataset with the same name
'''

def scan_directory_structure(directory_path):
    result = {}
    if os.path.isdir(directory_path):
        result[os.path.basename(directory_path)] = []
        for item in os.listdir(directory_path):
            item_path = os.path.join(directory_path, item)
            if os.path.isfile(item_path):
                result[os.path.basename(directory_path)].append(item)
            elif os.path.isdir(item_path):
                result[os.path.basename(directory_path)].append(scan_directory_structure(item_path))
    return result

def main(request):
    
    save_path = '/home/jupyter-ikharitonov/RANCZLAB-NAS/iakov/test_unzipped'
    
    # if this is a POST request we need to process the form data
    if request.method == "POST":
        # create a form instance and populate it with data from the request:
        form = DatasetForm(request.POST, request.FILES)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            
            # Create a database object
            new_dataset_unit = form.save(commit=False) # creates an incomplete (not all fields defined yet) instance, rather than saving to the database
            new_dataset_unit.date_added = timezone.now()
            
            # Check and unzip the uploaded file
            new_path = f"{save_path}/{new_dataset_unit.dataset_unit_name}"
            os.makedirs(new_path)
            file_name = str(form.cleaned_data['file'])
            if file_name.split('.')[1].lower() == 'zip':
                
                if zipfile.is_zipfile(form.cleaned_data['file']):
                    # Open the zip file
                    with zipfile.ZipFile(form.cleaned_data['file'], 'r') as zip_ref:
                        # Extract all contents to a temporary directory
                        # temp_dir = os.path.join(settings.MEDIA_ROOT, 'temp')
                        zip_ref.extractall(new_path)
                        
            # Complete the object fields with information related to unzipped content and save
            new_dataset_unit.content_path = new_path
            new_dataset_unit.directory_structure = str(scan_directory_structure(new_path))
            new_dataset_unit.save()
            
            display_content = f"Successfully saved dataset '{new_dataset_unit.dataset_unit_name}' at '{new_path}'"
            
            return render(request, "vector_injest/main.html", {"form": form, "display_output": True, "display_content": display_content})

    # if a GET (or any other method) we'll create a blank form
    else:
        form = DatasetForm()

    return render(request, "vector_injest/main.html", {"form": form})