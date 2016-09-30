from django.shortcuts import render
from django.contrib.auth.models import User
from django.shortcuts import render


def user_profile(request, user_id):
    user = User.objects.get(id=user_id)
    context = {'user': user}
    return render(request, 'user_profile/profile.html', context)
