# projects/views.py

from django.shortcuts import render
from projects.models import Project

# Create your views here.
def project_index(request):
    # (cRud) projects will store a Queryset of all projects in the table
    projects = Project.objects.all()
    context = {
        "projects": projects
    }
    return render(request, "projects/project_index.html", context)

def project_detail(request, pk):
    project = Project.objects.get(pk=pk)
    context = {
        "project": project
    }
    return render(request, "projects/project_detail.html", context)