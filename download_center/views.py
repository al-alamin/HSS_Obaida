from django.shortcuts import render
from .models import Type, Department, Document


def download(request, department_id=None):
    types = Type.objects.all().order_by('name')
    departments = Department.objects.all().order_by('name')
    context = {
        'types': types,
        'departments': departments
    }
    return render(request, 'download_center/download.html', context)
