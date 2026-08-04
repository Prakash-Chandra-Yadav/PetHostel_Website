from django.urls import path
from .views import HomeView, ContactCreateView, ReservationCreateView

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("contact/", ContactCreateView.as_view(), name="contact"),
    path("appointment/", ReservationCreateView.as_view(), name="appointment"),
]
