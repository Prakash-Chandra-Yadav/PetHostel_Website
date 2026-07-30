from django import forms
from .models import CustomerContact


class CustomerContactForm(forms.ModelForm):
    class Meta:
        model = CustomerContact
        fields = ["name", "contact_email", "pet_type", "message"]
