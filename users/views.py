from django.shortcuts import render
from django.template import loader
from .models import Cadet
from django.http import HttpResponse

# Create your views here.
def index(request):
    cadets = Cadet.objects.all() #Grab all cadets from database
    context = {'cadets': cadets} #fill a context with the cadet list
    template = loader.get_template('users/index.html') #Get the template we created
    return HttpResponse(template.render(context, request)) #Render the template with the context

def detail(request, cadet_id):
    try:
        cadet = Cadet.objects.get(pk=cadet_id)
    except Cadet.DoesNotExist:
        raise Http404("Cadet does not exist")
    return render(request, 'users/detail.html', {'cadet':cadet})


