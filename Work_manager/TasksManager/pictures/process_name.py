from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response

from .models import NewRegistrationForm

def process(request):
    print(request)

    if request.method == 'POST':
        form = NewRegistrationForm(request.POST)
        if form.is_valid():
            new_article = form.save()
            return HttpResponseRedirect('/thanks/')
        else:
            return render_to_response('en/public/index.html', {'form': form})
