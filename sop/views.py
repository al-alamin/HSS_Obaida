from django.contrib import messages
from django.shortcuts import render

from sop.forms import SOPSubmitForm
from sop.models import ReviewSubmission


def sop(request):
    email_success = False
    if request.method == 'POST':
        form = SOPSubmitForm(request.POST, request.FILES, user=request.user)
        if form.is_valid():
            file = request.FILES['file']
            email_success = form.email_SOP(file)
            if email_success:
                messages.success(request, "Your message was successfully sent!", 
                    extra_tags='alert-success')
                review_type = form.cleaned_data['review_type']
                # creating entry in review submission model to prevent multiple submission in one category
                ReviewSubmission.objects.create(user=request.user, review_type=review_type)

    else:
        data = dict()
        if request.user.is_authenticated:
            data = {'name': request.user.get_full_name(),
                    'email': request.user.email
                    }
        form = SOPSubmitForm(initial=data)

    context = {'form': form,
               'email_success': email_success,
               }
    return render(request, 'sop/sop_review.html', context)
