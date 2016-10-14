from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, redirect
from django.utils.timezone import now
from event.models import Event, Registration
from .forms import EventRegistrationForm, EventRegistrationDeleteForm


# Create your views here.
def skype(request):
    context = {}
    is_user_registered = False
    form = None
    del_form = None
    events = Event.objects.filter(start_time__gt=now(), event_type='skype_session')
    if events.exists():
        # take the first event ordered by start date. It's the first upcoming event
        event = events.first()
        context['event'] = event
        user = request.user
        # if event does not exist, there should be no registration
        # event registration must be available to be able to register
        if request.method == 'POST' and event.is_registration_open:
            form = EventRegistrationForm(request.POST)
            if form.is_valid():
                reg_success = form.save_and_mail(user=user, event=event)
                if reg_success:
                    messages.success(request,
                                     """Congratulations! You are registered for the event.
                                      A confirmation email will be sent to your email address momentarily""",
                                     extra_tags='alert-success')
                else:
                    messages.error(request, "Something went wrong. Please try again later", extra_tags='alert-danger')
        else:
            form = EventRegistrationForm()

        # Generate the delete form if user is registered
        if not user.is_anonymous():
            try:
                reg = Registration.objects.get(event=event, attendee=user)
            except ObjectDoesNotExist:
                is_user_registered = False
            else:
                is_user_registered = True
                initialdict = {'reg_id': reg.id}
                del_form = EventRegistrationDeleteForm(initialdict)

    context['is_user_registered'] = is_user_registered
    context['form'] = form
    context['del_form'] = del_form

    return render(request, 'skype_consultancy/skype_consultancy.html', context)


@login_required
def delete_skype_registration(request):
    if request.method == 'POST':
        form = EventRegistrationDeleteForm(request.POST)
        user = request.user
        if form.is_valid():
            del_success = form.del_registraion(user)
            if del_success:
                messages.success(request,
                                 'You registration is withdrawn from this event',
                                 extra_tags='alert-warning')

    return redirect('/skype/')
