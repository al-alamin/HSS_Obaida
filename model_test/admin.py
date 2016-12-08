from django.contrib import admin

from model_test.models import ModelTest, SubjectTest, MCQ, Result


class ModelTestAdmin(admin.ModelAdmin):
    list_display = ('name', 'exam_type', 'fee')
    list_filter = ('exam_type',)
    search_fields = ('name',)


class SubjectTestAdmin(admin.ModelAdmin):
    pass


class MCQAdmin(admin.ModelAdmin):
    pass


class ResultAdmin(admin.ModelAdmin):
    pass


admin.site.register(ModelTest, ModelTestAdmin)
admin.site.register(SubjectTest, SubjectTestAdmin)
admin.site.register(Result, ResultAdmin)
admin.site.register(MCQ, MCQAdmin)
