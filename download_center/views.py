from django.shortcuts import render
from .models import Type, Department, Document


def download(request, department_id=None):
    types = Type.objects.all().order_by('name').prefetch_related()
    if department_id is not None:
        types = types.filter(document__department__id = department_id)
    departments = Department.objects.all().order_by('name')
    context = {
        'types': types,
        'departments': departments,
        'department_id':department_id
    }
    return render(request, 'download_center/download.html', context)
