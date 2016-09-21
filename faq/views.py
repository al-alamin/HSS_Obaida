from django.shortcuts import render, redirect

from common import models
from .forms import FaqSearchForm
from .models import Question


def faq(request):
    types = models.Type.objects.all()
    recent_q = Question.objects.all().order_by('date_modified')[:50]
    popular_q = Question.objects.filter(is_popular=True).order_by('date_modified')[:50]
    faq_search_form = FaqSearchForm()
    context = {'types': types,
               'recent_q': recent_q,
               'popular_q':popular_q,
               'faq_search_form': faq_search_form,
               }
    return render(request, 'faq/faq.html', context)


def search_result(request, cat_id=None, tag_id=None):
    # News and Blog should not be added in FAQ page
    # used to populate categories and tags arranged by their type
    types = models.Type.objects.all().exclude(name='News')
    faq_search_form = FaqSearchForm()
    search_for = ''
    if request.method == 'POST':
        faq_search_form = FaqSearchForm(request.POST)
        if faq_search_form.is_valid():
            search_for = faq_search_form.cleaned_data['search_item']
            if search_for:
                search_result = faq_search_form.get_search_result()
            else:
                redirect('faq')

    elif cat_id is not None:
        search_result = Question.objects.filter(category__id=cat_id)
        search_for = models.Category.objects.get(id=cat_id).name + ' Category'
    elif tag_id is not None:
        search_result = Question.objects.filter(tag__id=tag_id)
        search_for = models.Tag.objects.get(id=tag_id).name + ' Tag'
    else:
        redirect('faq')

    context = {
        'faq_search_form': faq_search_form,
        'search_result': search_result,
        'types': types,
        'search_for': search_for,
    }
    return render(request, 'faq/search_result.html', context)
