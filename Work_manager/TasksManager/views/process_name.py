from django.http import HttpResponseRedirect
from django.core.mail import send_mail
from .forms import RegistrationForm
from django.shortcuts import render_to_response

def process(request):
    print(request)

    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            sender = form.cleaned_data['sender']
            cc_myself = form.cleaned_data['cc_myself']

            recipients = ['info@example.com']
            if cc_myself:
                recipients.append(sender)

            send_mail(subject, message, sender, recipients)
            return HttpResponseRedirect('/thanks/')
        else:
            return render_to_response('en/public/index.html', {'form': form})
