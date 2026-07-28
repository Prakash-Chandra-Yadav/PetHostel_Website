from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Contact


# Create your views here.
class HomeView(TemplateView):
    template_name = "home.html"


class ContactView(TemplateView):
    template_name = "contact.html"
