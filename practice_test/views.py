from django.shortcuts import render
from django.views import View

class GreView(View):

    template_name = 'practice_test/gre.html'

    def get(self, request, *args, **kwargs):

        return render(request, self.template_name)

    def post(self, request, *args, **kwargs):
        pass
