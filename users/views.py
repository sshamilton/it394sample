from django.shortcuts import render
from django.template import loader
from .models import Cadet
from .models import Company
from django.http import HttpResponse
from django.http import HttpResponseRedirect

from .forms import CadetForm
from .forms import CompanyForm
from django.contrib.auth.decorators import permission_required
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    cadets = Cadet.objects.all() #Grab all cadets from database
    context = {'cadets': cadets} #fill a context with the cadet list
    template = loader.get_template('users/index.html') #Get the template we created
    return HttpResponse(template.render(context, request)) #Render the template with the context

def detail(request, cadet_id):
    try:
        cadet = Cadet.objects.get(pk=cadet_id)
        companies = Company.objects.all()
        context = {'cadet':cadet, 'companies': companies}
    except Cadet.DoesNotExist:
        raise Http404("Cadet does not exist")
    return render(request, 'users/detail.html', context)

def update(request, cadet_id):
    new_xnumber = request.POST['xnumber']
    new_company_id = request.POST['company_id']
    cadet = Cadet.objects.get(pk=cadet_id)
    cadet.xnumber = new_xnumber
    cadet.company_id = new_company_id
    cadet.save()
    companies = Company.objects.all()
    context = {'cadet':cadet, 'companies': companies}
    return render(request, 'users/detail.html', context)

def addcadet(request):
    #if user.has_perm('cadet.add_cadet'):
    if request.method == 'POST':
        form = CadetForm(request.POST)
        if form.is_valid():
            #Add the cadet to the database
            newcadet = form.save()
            #Go back to cadet list
            return HttpResponseRedirect('/users')
    else:
        form = CadetForm()
    return render(request, 'users/add.html', {'form': form})
    #else:
        #return HttpResponseRedirect('/users')

def addcompany(request):
    #if user.has_perm('cadet.add_cadet'):
    if request.method == 'POST':
        form = CompanyForm(request.POST)
        if form.is_valid():
            #Add the cadet to the database
            newcompany = form.save()
            #Go back to cadet list
            return HttpResponseRedirect('/users')
    else:
        form = CompanyForm()
    return render(request, 'users/add.html', {'form': form})
