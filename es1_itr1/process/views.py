from django.shortcuts import render, get_object_or_404

from input.models import DatasetUnit

import ast

# Create your views here.

def main(request):
    print(DatasetUnit.objects.all())
    return render(request, "process/main.html")

def front_page_view(request):
    return render(request, "process/front_page.html")

def view(request):
    output_list = [db for db in DatasetUnit.objects.all()]
    return render(request, "process/view.html", {"output_list": output_list})

def generate_html(directory_structure, indent_level=0):
    if indent_level == 0: directory_structure = [directory_structure]
    html = ""
    for elem in directory_structure:
        if isinstance(elem, dict):
            for folder_name, contents in elem.items():
                # Add folder name with appropriate indentation
                html += f"<div style='margin-left: {indent_level * 20}px;'>{folder_name}/</div>"
                html += generate_html(contents, indent_level + 1)
        elif isinstance(elem, str):
            html += f"<div style='margin-left: {(indent_level + 1) * 20}px;'>{elem}</div>"
        else:
            raise TypeError('Unsupported format encountered within saved directory structure of the dataset.')
    return html

def detail_dataset(request, pk, object_name):
    model_object = get_object_or_404(DatasetUnit, pk=pk)
    parsed_directory_structure = ast.literal_eval(model_object.directory_structure)
    directory_structure_html = generate_html(parsed_directory_structure)
    return render(request, 'process/detail.html', {'dataset': model_object, 'directory_structure_html': directory_structure_html})