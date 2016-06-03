from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.
# - * - Coding: utf -8 - * -
#sys.path.insert(0, os.path.abspath('.'))
# View for index page.
from .models import PictureForm, PictureModel
def upload_pictures (request):
    #return HttpResponse ("Hello world new!" )
    if request.method == 'POST':
        picture = PictureModel(request.POST, request.FILES)
        picture.save()
    else:
        picture = PictureModel()
    return render(request, 'UploadPictures.html', {'form': PictureForm})

def display_pictures (request):
    query_results = PictureModel.objects.all()
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

    return render(request, 'DisplayPictures.html', {'query_results':doctors})