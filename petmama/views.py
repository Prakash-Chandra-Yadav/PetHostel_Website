from django.shortcuts import render
from django.views.generic import TemplateView, CreateView
from .models import Contact, CustomerContact


# Create your views here.
class HomeView(TemplateView):
    template_name = "home.html"


class ContactView(TemplateView):
    template_name = "contact.html"


class ContactCreateView(CreateView):
    model = CustomerContact
    template_name = "contact.html"
    fields = ["name", "contact_email", "pet_type", "message"]
