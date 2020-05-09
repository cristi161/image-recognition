from django.shortcuts import render
from django.http import  HttpResponse
from django.shortcuts import redirect
from .models import *
from .forms import *
from django.core.files.storage import FileSystemStorage
from django.views.generic import TemplateView
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .forms import CreateUserForm
# Create your views here.

def pagina(request): #Functia principa;a care ajuta la randarea paginii plus functiile de login and singup
    form = CreateUserForm()  #SINGUP
    if request.method == 'POST' and request.POST.get('signup') == '':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account was created')

    if request.method == 'POST' and request.POST.get('login') == '':  #login
        username = request.POST.get('username_login')
        password = request.POST.get('password_login')
        email = request.POST.get
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('login-page')
        else:
            messages.info(request, 'Username or password is incorrect')
    def logout(request):
        logout(request)
        return redirect('site_web')
    login_required(login_url='site-web')


    context = {'form': form}
    return  render(request, 'charecog.html', context)



def loginpage(request):
    if request.method == 'POST' and request.POST.get('upload') == '':  # Acest if se ocupa de upload si save a imaginilor!!
        uploaded_file = request.FILES['document']
        fs = FileSystemStorage()
        fs.save(uploaded_file.name, uploaded_file)


    def logout(request):
        logout(request)
        return redirect('site_web')

    login_required(login_url='site-web')

    return render(request, 'recologin.html',{})

def aboutpage(request):
    return render(request, 'about.html')
