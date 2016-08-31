from django import forms
from django.db.models import Q

from common import models


class FaqSearchForm(forms.Form):
    attrs = {"class": "form-control", "placeholder": "search", "required": "required"}
    search_item = forms.CharField(max_length=50, min_length=1, widget=forms.TextInput(attrs=attrs))

    def get_search_result(self):
        item = self.cleaned_data['search_item']
        if len(item) > 0 and item != '':
            q = models.Question.objects.filter(
                Q(text__icontains=item) |
                Q(answer__text__icontains=item) |
                Q(category__name__icontains=item) |
                Q(tag__name__icontains=item)).distinct()
            return q
        else:
            return None
