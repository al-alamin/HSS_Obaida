from django.contrib import admin

from gre_practice_test.models import GreModelTest, GreSubjectTest, GreMCQ, GreSubjestTestResult


class GreModelTestAdmin(admin.ModelAdmin):
    list_display = ('name', 'fee')
    search_fields = ('name',)


class GreSubjectTestAdmin(admin.ModelAdmin):
    pass


class GreMCQAdmin(admin.ModelAdmin):
    pass


class GreSubjestTestResultAdmin(admin.ModelAdmin):
    pass


admin.site.register(GreModelTest, GreModelTestAdmin)
admin.site.register(GreSubjectTest, GreSubjectTestAdmin)
admin.site.register(GreSubjestTestResult, GreSubjestTestResultAdmin)
admin.site.register(GreMCQ, GreMCQAdmin)
