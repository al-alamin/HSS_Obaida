from django.shortcuts import render, redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from common import models
from .forms import FaqSearchForm
from .models import Question


def get_pages_to_show(paginator, page):
    ''' 
        Pagination link will show
        previous button
        first page always
        two pages before selected page
        the selected page
        two pages after selected page
        last page always
        next button

        suppose there is total 100 page. you want to see page 20
        then the pages to show list will be [1, -1, 18,19,20,21,22,-1, 100]
        -1 indicated .. ie skipping pages_to_show
        you want to see page 100
        then the pages to show list will be [1, -1, 98, 99, 100]

    '''
    page = int(page)
    # As it is a set duplicate entries will be discarded
    pages_wanted = set([1,
                        page-2, page-1,
                        page,
                        page+1, page+2,
                        paginator.num_pages])

    # The intersection with the page_range trims off the invalid
    # pages outside the total number of pages we actually have will be
    # discarded.
    pages_to_show = set(paginator.page_range).intersection(pages_wanted)
    pages_to_show = sorted(pages_to_show)

    # skip pages will in the pages to show list where to put .. ie -1
    skip_pages = []
    for i in range(len(pages_to_show) - 1):
        # if the list is not incrementing normally then there is a gap ie .. ie -1 is needed
        if((pages_to_show[i+1] - pages_to_show[i]) != 1):
            skip_pages.append(pages_to_show[i+1])
   
    # Each page in skip_pages should be follwed by -1 to identify ...
    # now appending -1 in the pages to show list. in the template when -1 is found .. will be printed
    for i in skip_pages:
        pages_to_show.insert(pages_to_show.index(i), -1)

    return pages_to_show


def get_page(paginator, page):

    try:
        pagination_page = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        page = 1
        pagination_page = paginator.page(page)

    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        page = paginator.num_pages
        pagination_page = paginator.page(page)

    return pagination_page


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
    # this is for which page no of the request to send to the user
    page = 1
    # when user clicks on pagination page links there there will be a get request
    if request.method == 'GET':
        page = request.GET.get('page', 1)
        # getting previously stored search keyword from session variable
        search_for = request.session.get('search_for')
        if(search_for):
            faq_form = FaqSearchForm(data={'search_item': search_for})
            if(faq_form.is_valid()):
                search_result = faq_form.get_search_result()
        else:
            return redirect('faq')

    # when the user search using the search box then there will be a post
    # request.
    elif request.method == 'POST':
        faq_search_form = FaqSearchForm(request.POST)
        if faq_search_form.is_valid():
            search_for = faq_search_form.cleaned_data['search_item']
            if search_for:
                # saving query key word to session variable
                request.session['search_for'] = search_for
                search_result = faq_search_form.get_search_result()
            else:
                return redirect('faq')

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
        return redirect('faq')

    # https://docs.djangoproject.com/en/1.10/topics/pagination/
    # This part is need for pagination
    item_per_page = 1

    # objects = [x for x in range(0,1000)]
    paginator = Paginator(search_result, item_per_page)
    # going to get the list of page no to show in the pagination links
    pages_to_show = get_pages_to_show(paginator, page)
    # getting limitted search result from full result by pagination
    search_result_pagination = get_page(paginator, page)
    context = {
        'faq_search_form': faq_search_form,
        'types': types,
        'search_for': search_for,
        'is_single': is_single,
        'search_result_pagination': search_result_pagination,
        'pages_to_show': pages_to_show
    }
    return render(request, 'faq/search_result.html', context)
