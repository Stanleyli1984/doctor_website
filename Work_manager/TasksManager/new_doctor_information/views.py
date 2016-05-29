from django.shortcuts import render

# Create your views here.
# - * - Coding: utf -8 - * -
#sys.path.insert(0, os.path.abspath('.'))
# View for index page.
from .models import NewRegistrationForm, NewRegistrationModel
def add_doctor (request):
    #return HttpResponse ("Hello world new!" )
    return render(request, 'en/public/index.html', {'form': NewRegistrationForm})

def display_doctors (request):
    query_results = NewRegistrationModel.objects.all()
    return render(request, 'doctors.html', {'query_results':query_results})