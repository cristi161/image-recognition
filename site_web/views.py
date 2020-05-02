from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from .models import *
from .forms import *
from django.core.files.storage import FileSystemStorage
from django.views.generic import TemplateView
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model

# Create your views here.


def pagina(request):
    print("start of page")
    if request.method == 'POST' and request.POST.get('upload') == '': #Acest if se ocupa de upload si save a imaginilor!!
        uploaded_file = request.FILES['document']
        fs = FileSystemStorage()
        fs.save(uploaded_file.name, uploaded_file)
        #de aici ar trebui sa porneasca alg detect !!!!!

    if request.method == 'POST' and request.POST.get('signup') == '':
        username = request.POST.get('username')
        password = request.POST.get('password')


    return render(request, 'charecog.html', {'form': UserCreationForm()})





