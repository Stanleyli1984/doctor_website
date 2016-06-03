from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponseRedirect


# Create your views here.
# - * - Coding: utf -8 - * -
#sys.path.insert(0, os.path.abspath('.'))
# View for index page.
from .models import PictureForm, PictureModel
def upload_pictures (request):
    #return HttpResponse ("Hello world new!" )
    if request.method == 'POST':
        picture_form = PictureForm(request.POST, request.FILES)
        if picture_form.is_valid():
            # Is there any way not to explicitly list every field?
            newdoc = PictureModel(name=request.POST['name'], docfile=request.FILES['docfile'])
            newdoc.save()
            return HttpResponseRedirect('/thanks/')
    else:
        picture_form = PictureForm()
    return render(request, 'UploadPictures.html', {'form': picture_form})

def display_pictures (request):
    query_results = PictureModel.objects.all()
    paginator = Paginator(query_results, 2)

    page = request.GET.get('page')  # can get from request
    try:
        pictures = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        pictures = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        pictures = paginator.page(paginator.num_pages)

    return render(request, 'DisplayPictures.html', {'query_results':pictures})