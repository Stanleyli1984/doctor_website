from django.shortcuts import render

# Create your views here.
# - * - Coding: utf -8 - * -
#sys.path.insert(0, os.path.abspath('.'))
# View for index page.
from TasksManager.views.forms import RegistrationForm
def page (request):
    #return HttpResponse ("Hello world new!" )
    return render(request, 'en/public/index.html', {'form': RegistrationForm})

