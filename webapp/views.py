from django.shortcuts import render
from django.http import  HttpResponse
from django.shortcuts import redirect
from .models import *
from .forms import *
from django.core.files.storage import FileSystemStorage
from django.views.generic import TemplateView
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login , logout
from .forms import CustomUserForm
from PIL import Image
import pytesseract as tess
import textd as alg
import carplate as algcar
from django.contrib import messages
import OCR as oc
from django.http import FileResponse
# Create your views here.


def pagina(request):
    form2 = CustomUserForm()
    if request.method == 'POST' and request.POST.get('signup') == '':
        print("if mare")
        form2 = CustomUserForm(request.POST)
        if form2.is_valid():
            print("form is valid")
            form2.save()
            messages.success(request, 'Account was created')

    if request.method == 'POST' and request.POST.get('login') == '':  #login
        username = request.POST.get('username_login')
        password = request.POST.get('password_login')
       # email = request.POST.get
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('choosealg')
        else:
            messages.info(request, 'Username or password is incorrect')
    def logout(request):
        logout(request)
        return redirect('webapp')
    login_required(login_url='webapp')

    context = {'form': form2}
    return  render(request, 'charecog.html', context)


def loginpage(request):
    file_name = "dsafdsafas"
    text = ""
    founded = ''
    if request.method == 'POST' and request.POST.get('upload') == '':  # Acest if se ocupa de upload si save a imaginilor!!
        uploaded_file = request.FILES['document']
        fs = FileSystemStorage()
        fs.save(uploaded_file.name, uploaded_file)
        print(uploaded_file.name)
        file_name = alg.detecfunc("/Users/mmm/Desktop/image-recognition-site-web-5-0/media/"+uploaded_file.name)
        text = tess.image_to_string((Image.open(uploaded_file)))
        print(text)
        founded = 'found'
        file = open("/Users/mmm/Desktop/image-recognition-site-web-5-0/static/text_from_picture.txt", "w")
        file.write(text)
        file.close()

    context = {'img_name': 'img_detect/' + file_name, 'img_text': text, 'founded': founded}
    print('final')
    return render(request, 'recologin.html', context)


    def logout(request):
        logout(request)
        return redirect('webapp')

    login_required(login_url='webapp')

    return render(request, 'recologin.html',{})

def aboutpage(request):
    form = CustomUserForm()
    if request.method == 'POST' and request.POST.get('signup') == '':
        print("if mare")
        form = CustomUserForm(request.POST)
        if form.is_valid():
            print("form is valid")
            form.save()
            messages.success(request, 'Account was created')

    if request.method == 'POST' and request.POST.get('login') == '':  # login
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
            return redirect('webapp')

        login_required(login_url='webapp')
    context = {'form': form}

    return render(request, 'about.html', context)



def tologinPage(request):
    if request.method == 'POST':
        username = request.POST.get('your_name')
        password = request.POST.get('your_pass')
        user = authenticate(request, username = username, password = password)
        if user is not None:
            login(request, user)
            return redirect('choosealg')
        else:
            messages.info(request, 'Username or password is incorrect')

    context = {}
    return render(request, 'login.html', context)

def register2(request):
    form = CustomUserForm()
    if request.method == 'POST':
        form = CustomUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Account was created for ' + user )

            return redirect('tologin')
    context = {'form': form}

    return render(request, 'singup2.html', context)
def logoutUser(request):
    logout(request)
    return redirect('webapp')


def choosealg(request):
    login_required(login_url='webapp')

    return  render(request, 'choosealg.html')

def logoutUser(request):
    logout(request)
    return redirect('webapp')


def carplate(request):
    file_name = "dsafdsafas"
    text = ""
    founded = ''
    if request.method == 'POST' and request.POST.get('upload') == '':  # Acest if se ocupa de upload si save a imaginilor!!
        uploaded_file = request.FILES['document']
        fs = FileSystemStorage()
        fs.save(uploaded_file.name, uploaded_file)
        print(uploaded_file.name)
        file_name = algcar.detectplate("/Users/mmm/Desktop/image-recognition-site-web-5-0/media/" + uploaded_file.name)
        text = tess.image_to_string((Image.open(uploaded_file)))
        print(text)
        founded = 'found'
        file = open("/Users/mmm/Desktop/image-recognition-site-web-5-0/static/text_from_picture.txt", "w")
        file.write(text)
        file.close()

    context = {'img_name':  file_name, 'img_text': text, 'founded': founded}
    print('final')

    login_required(login_url='webapp')

    return render(request, 'carplate.html', context)

def logoutUser(request):
    logout(request)
    return redirect('webapp')
