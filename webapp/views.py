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
from .forms import CreateUserForm
from PIL import Image
import pytesseract as tess
import textd as alg
import OCR as oc
from django.http import FileResponse
# Create your views here.


def pagina(request):
    form = CreateUserForm()
    if request.method == 'POST' and request.POST.get('signup') == '':
        print("if mare")
        form = CreateUserForm(request.POST)
        if form.is_valid():
            print("form is valid")
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
        return redirect('webapp')
    login_required(login_url='webapp')

    context = {'form': form}
    return  render(request, 'charecog.html', context)

form = CreateUserForm()
def loginpage(request):
    file_name = "dsafdsafas"
    text = ""
    if request.method == 'POST' and request.POST.get('upload') == '':  # Acest if se ocupa de upload si save a imaginilor!!
        uploaded_file = request.FILES['document']
        fs = FileSystemStorage()
        fs.save(uploaded_file.name, uploaded_file)
        print(uploaded_file.name)
        alg.detecfunc("/Users/mmm/Desktop/image-recognition-site-web-2-0/media/"+uploaded_file.name)
        file_name = uploaded_file.name
        text = tess.image_to_string((Image.open(uploaded_file)))
        print(text)
        file = open("text_from_picture.txt", "a+")
        file.write(text)
        file.close()

    context = {'form': form, 'img_name': file_name, 'img_text': text}
    print('final')
    return  render(request, 'recologin.html', context)


    def logout(request):
        logout(request)
        return redirect('webapp')

    login_required(login_url='webapp')

    return render(request, 'recologin.html',{})

def aboutpage(request):
    form = CreateUserForm()
    if request.method == 'POST' and request.POST.get('signup') == '':
        print("if mare")
        form = CreateUserForm(request.POST)
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


    return render(request, 'about.html')

