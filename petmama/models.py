from django.db import models


# Create your models here.
class Contact(models.Model):
    location = models.TextField(max_length=50)
    phone_number = models.TextField(max_length=18)
    email = models.EmailField()

    def __str__(self):
        return self.location


class CustomerContact(models.Model):
    class PetType(models.TextChoices):
        DOG = "dog", "Dog"
        CAT = "cat", "Cat"
        OTHER = "other", "Other"

    name = models.TextField(max_length=30)
    contact_email = models.EmailField()
    pet_type = models.CharField(max_length=10, choices=PetType.choices)
    message = models.TextField(max_length=200)

    def __str__(self):
        return self.name


class Reservation(models.Model):
    class PetType(models.TextChoices):
        DOG = "dog", "Dog"
        CAT = "cat", "Cat"
        OTHER = "other", "Other"

    checkin_date = models.DateField()
    checkout_date = models.DateField()
    pet_name = models.TextField(max_length=21)
    pet_age = models.PositiveBigIntegerField()
    parent_name = models.TextField(max_length=21)
    contact_number = models.TextField(max_length=14)
    booking_email = models.EmailField()
    pet_type = models.CharField(max_length=10, choices=PetType.choices)

    def _str__(self):
        return self.parent_name
