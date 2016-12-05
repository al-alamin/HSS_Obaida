from django.shortcuts import render, redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from common import models
from .forms import FaqSearchForm
from .models import Question


def faq(request):
    types = models.Type.objects.all()
    recent_q = Question.objects.all().order_by('date_modified')[:50]
    popular_q = Question.objects.filter(
        is_popular=True).order_by('date_modified')[:50]
    faq_search_form = FaqSearchForm()
    context = {'types': types,
               'recent_q': recent_q,
               'popular_q': popular_q,
               'faq_search_form': faq_search_form,
               }
    return render(request, 'faq/faq.html', context)


def search_result(request, question_id=None, cat_id=None, tag_id=None):
    # News and Blog should not be added in FAQ page
    # used to populate categories and tags arranged by their type
    types = models.Type.objects.all().exclude(name='News')
    faq_search_form = FaqSearchForm()
    search_for = ''
    is_single = False
    search_result = ""
    # This part will return search result when user types and searches faq from searchbox
    if request.method == 'POST':
        faq_search_form = FaqSearchForm(request.POST)
        # when user clicks on pagination links though that will be a post request but this faq_form will be invalid
        # so search_result will not be generated from here
        if faq_search_form.is_valid():
            search_for = faq_search_form.cleaned_data['search_item']
            if search_for:
                search_result = faq_search_form.get_search_result()
            else:
                redirect('faq')

    elif question_id is not None:
        search_result = Question.objects.filter(id=question_id)
        search_for = 'Single Question'
        is_single = True
    elif cat_id is not None:
        search_result = Question.objects.filter(category__id=cat_id)
        search_for = models.Category.objects.get(id=cat_id).name + ' Category'
    elif tag_id is not None:
        search_result = Question.objects.filter(tag__id=tag_id)
        search_for = models.Tag.objects.get(id=tag_id).name + ' Tag'
    else:
        redirect('faq')

    # https://docs.djangoproject.com/en/1.10/topics/pagination/
    # This part is need for pagination
    item_per_page = 2
    # when user clicks on pagination links like next/previous button or 1,2,... page number then there will be
    # a get url with page associated with it
    # when users types and search this page will be none and search_result
    # will be generated from faq_search from.
    page = request.GET.get('page')
    # This part will return search result when user clicks on pagination links like next/previous button or
    # 1,2,... page number
    if(page):
        search_for = request.POST.get('search_name')
        f_s_form = FaqSearchForm(data={'search_item': search_for})
        f_s_form.is_valid()
        search_result = f_s_form.get_search_result()

    # after we have gotten the search result either from faq_search_form or pagination form
    # Here the pagination will be done.
    paginator = Paginator(search_result, item_per_page)
    try:
        search_result_pagination = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        search_result_pagination = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        search_result_pagination = paginator.page(paginator.num_pages)

    context = {
        'faq_search_form': faq_search_form,
        'search_result': search_result,
        'types': types,
        'search_for': search_for,
        'is_single': is_single,
        'search_result_pagination': search_result_pagination,
    }
    return render(request, 'faq/search_result.html', context)
