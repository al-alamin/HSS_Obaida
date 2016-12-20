from django.shortcuts import render
from django.views import View
from django.http import HttpResponse

from gre_practice_test.models import GreSubjectTest, GreMCQ


class IndexView(View):

    template_name = 'gre_practice_test/index.html'

    def get(self, request, *args, **kwargs):
        subject_test = GreSubjectTest.objects.all()
        context = {
            'subject_test': subject_test,
        }
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        pass


class GreSubjectTestRulesView(View):

    template_name = 'gre_practice_test/rules.html'

    def get(self, request, *args, **kwargs):
        subject_test_id = self.kwargs['id']
        subject_test = GreSubjectTest.objects.get(id=subject_test_id)
        context = {
            'subject_test': subject_test,
        }
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        pass

class GreSubjectTestExamView(View):

    template_name = 'gre_practice_test/gre_subject_test_exam.html'

    def get(self, request, *args, **kwargs):
        subject_test_id = self.kwargs['id']
        subject_test = GreSubjectTest.objects.get(id=subject_test_id)
        mcq_list = GreMCQ.objects.filter(subject_test=subject_test)
        total_time = int(len(mcq_list) * 60 * 1.5)
        context = {
            'subject_test': subject_test,
            'mcq_list': mcq_list,
            'total_time': total_time,
        }
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):

        return HttpResponse("Exam is over.")