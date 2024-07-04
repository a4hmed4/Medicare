from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
#from django.http import HttpResponse
from .models import patient
from .models import profile



# Create your views here.


def index(request):
   #pass
   #x = {'name':'ahmed', 'age':19}
   return render(request, "patients/pages/index.html")

def about(request):
    #pass
    return render(request, 'patients\Home\profile\profile.html', {'prof':profile.objects.all()})
    
def home(request):
    #pass
    return render(request, 'patients\Home\patientshome\patientshome.html', {'pat':patient.objects.all()})

