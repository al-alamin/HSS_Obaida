from django import forms
from django.db.models import Q

from .models import Question
from django.contrib.postgres.search import SearchQuery,\
    SearchRank, SearchVector


class FaqSearchForm(forms.Form):
    attrs = {"class": "form-control",
             "placeholder": "search", "required": "required"}
    search_item = forms.CharField(
        max_length=50, min_length=1, widget=forms.TextInput(attrs=attrs))

    # for details
    # https://docs.djangoproject.com/en/1.10/ref/contrib/postgres/search/
    def get_search_result(self):
        item = self.cleaned_data['search_item']
        if len(item) > 0 and item != '':
            # SearchVector allows to search on multiple field where is prioty
            # A, B, C, D  ... A highest D lowest priority
            vector = SearchVector(
                'text', weight='A') + SearchVector('ans', weight='B')

            ''' 
                Search Querry allows to make multiple search.
                First we'll try to match the whole sentence then we'll 
                also try to find result with parts of search sentence.
                This split will break the search sentence into multiple word
            '''

            # quering with full search sentence
            query = SearchQuery(item)
            # quering with parts(word) of the search text(sentence)
            for word in item.split():
                query = query | SearchQuery(word)
            q = Question.objects.annotate(rank=SearchRank(
                vector, query)).filter(rank__gt=0).order_by('-rank')

            return q
        else:
            return None
