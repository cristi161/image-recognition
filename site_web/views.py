from django.shortcuts import render
from django.http import  HttpResponse
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

  #  if request.method == 'POST' and request.POST.get('upload') == '': #Acest if se ocupa de upload si save a imaginilor!!
        #uploaded_file = request.FILES['document']
        #fs = FileSystemStorage()
       # fs.save(uploaded_file.name, uploaded_file)
        #de aici ar trebui sa porneasca alg detect !!!!!
    form = UserCreationForm()

    if request.method == 'POST' and request.POST.get('signup') =='':
        print("if mare")
        form = UserCreationForm(request.POST)
        if form.is_valid():
            print("form is valid")
            form.save()

    context = {'form': form}
    print('final')
    return  render(request, 'charecog.html', context)





