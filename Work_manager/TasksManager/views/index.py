import sys, os
from django.shortcuts import render

# Create your views here.
# - * - Coding: utf -8 - * -
from django.http import HttpResponse
#sys.path.insert(0, os.path.abspath('.'))
# View for index page.
from .forms import RegistrationForm
def page (request):
    #return HttpResponse ("Hello world new!" )
    return render(request, 'en/public/index.html', {'form': RegistrationForm})

