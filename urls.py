from django.urls import path
from AplicacionesApp import views
from . import views

urlpatterns = [
    path('', views.contacto, name="Contacto"),
]
