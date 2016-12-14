from django.shortcuts import render


# Create your views here.
def practice_test(request):
    return render(request, 'practice_test/practice_test.html')
