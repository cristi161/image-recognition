from django.urls import  path
from webapp import views

urlpatterns = [
    path('', views.pagina, name = 'webapp'),
    path('login-page', views.loginpage, name = 'login-page'),
    path('about', views.aboutpage, name='about'),
    path('tologin', views.tologinPage, name ='tologin'),
    path('register', views.register2, name='register'),

]