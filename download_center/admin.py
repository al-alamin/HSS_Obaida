from django.contrib import admin
from .models import Type, Department, Document

admin.site.register((Type, Department, Document))
