from django.urls import  path
from site_web import views

urlpatterns = [
    path('', views.pagina, name = 'site_web'),

]