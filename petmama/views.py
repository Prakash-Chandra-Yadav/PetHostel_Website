from django.shortcuts import render
from django.views.generic import TemplateView, CreateView
from .models import Contact, CustomerContact
from .forms import CustomerContactForm
from django.contrib import messages
from django.urls import reverse_lazy


# Create your views here.
class HomeView(TemplateView):
    template_name = "home.html"


class ContactCreateView(CreateView):
    model = CustomerContact
    template_name = "contact.html"
    fields = ["name", "contact_email", "pet_type", "message"]
    success_url = reverse_lazy("contact")

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, "Thanks! we will be in touch soon")
        return response
    
class ReserveCreateView(CreateView):
    
