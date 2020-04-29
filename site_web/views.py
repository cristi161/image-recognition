from django.shortcuts import render
from django.http import  HttpResponse
from django.shortcuts import redirect
from .models import *
from .forms import *
from django.core.files.storage import FileSystemStorage
from django.views.generic import TemplateView
# Create your views here.

class Home(TemplateView):
    template_name = 'home.html'

def pagina(request):
    if request.method == 'POST':
        uploaded_file = request.FILES['document']
        fs = FileSystemStorage()
        fs.save(uploaded_file.name, uploaded_file)
    return  render(request, 'charecog.html', {})

def aboutpagina(request):
    return render(request, 'about.html', {})

