from django import forms
from .models import CustomerContact, Reservation


class CustomerContactForm(forms.ModelForm):
    class Meta:
        model = CustomerContact
        fields = ["name", "contact_email", "pet_type", "message"]


class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = [
            "checkin_date",
            "checkout_date",
            "pet_name",
            "pet_age",
            "parent_name",
            "contact_number",
            "booking_email",
            "pet_type",
        ]
