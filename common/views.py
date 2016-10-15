from django.shortcuts import render


def under_construction_page(request):
    return render(request, 'common/under_construction_page.html')


def login(request):
    next_url = request.GET.get('next', '#')
    return render(request, 'common/login.html', {'next_url': next_url})
