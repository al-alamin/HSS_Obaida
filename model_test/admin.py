from django.contrib import admin

from model_test.models import ModelTest


class ModelTestAdmin(admin.ModelAdmin):
    list_display = ('name', 'exam_type', 'fee')
    list_filter = ('exam_type',)
    search_fields = ('name',)



admin.site.register(ModelTest, ModelTestAdmin)
