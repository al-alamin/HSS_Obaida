from django.contrib.auth.models import User
from random import shuffle
from django.shortcuts import render


def home(request):
    advisors_roles = ['Advisor', 'Reviewer', 'Presenter']
    advisors = User.objects.filter(groups__name__in=advisors_roles).distinct()
    # want the advisors list to appear in random. so people will not see same faces every time
    advisors = (list(advisors))  # to make it shuffleable
    shuffle(advisors)  # in-place shuffling
    return render(request, "home/home.html", {'advisors': advisors})


def decision_making(request):
    return render(request, "home/decision_making.html")


def preparation(request):
    return render(request, "home/preparation.html")


def standard_exam(request):
    return render(request, "home/standard_exam.html")

def application(request):
    return render(request, "home/application.html")


def google_custom_search(request):
    return render(request, 'google_custom_search/custom_search.html')
