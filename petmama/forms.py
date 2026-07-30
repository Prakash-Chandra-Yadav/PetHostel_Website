from django import forms
from .models import CustomerContact


class CustomerContactForm(forms.ModelForm):
    class meta:
        model = CustomerContact
        fields = ["name", "contact_email", "pet_type", "message"]
