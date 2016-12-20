# from django.shortcuts import render
# from django.views import View
# from django.http import HttpResponse

# from practice_test.models import SubjectTest




# class GreView(View):

#     template_name = 'practice_test/gre.html'

#     def get(self, request, *args, **kwargs):
#         subject_test = SubjectTest.objects.filter(exam_type='gre')
#         context = {
#             'subject_test': subject_test,
#         }
#         return render(request, self.template_name, context)

#     def post(self, request, *args, **kwargs):
#         pass


# class GreSubjectTestRulesView(View):

#     template_name = 'practice_test/gre_subject_test_rules.html'

#     def get(self, request, *args, **kwargs):
#         subject_test_id = self.kwargs['id']
#         subject_test = SubjectTest.objects.get(id=subject_test_id)
#         context = {
#             'subject_test': subject_test,
#         }
#         return render(request, self.template_name, context)

#     def post(self, request, *args, **kwargs):
#         pass


# class GreSubjectTestExamView(View):

#     template_name = 'practice_test/gre_subject_test_exam.html'

#     def get(self, request, *args, **kwargs):
#         subject_test_id = self.kwargs['id']
#         subject_test = SubjectTest.objects.get(id=subject_test_id)
#         mcq_list = MCQ.objects.filter(subject_test=subject_test)
#         total_time = int(len(mcq_list) * 60 * 1.5)
#         context = {
#             'subject_test': subject_test,
#             'mcq_list': mcq_list,
#             'total_time': total_time,
#         }
#         return render(request, self.template_name, context)

#     def post(self, request, *args, **kwargs):

#         return HttpResponse("Exam is over.")
