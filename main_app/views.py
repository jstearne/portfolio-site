from django.shortcuts import render, redirect, reverse
from django.views import View  # <- View class to handle requests
# <- a class to handle sending a type of response
from django.http import HttpResponse
from django.views.generic.base import TemplateView

# Create your views here.
class Home(TemplateView):
    template_name = "home.html"