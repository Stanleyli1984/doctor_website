from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

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
    paginator = Paginator(query_results, 2)

    page = request.GET.get('page')  # can get from request
    try:
        doctors = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        doctors = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        doctors = paginator.page(paginator.num_pages)

    return render(request, 'doctors.html', {'query_results':doctors})