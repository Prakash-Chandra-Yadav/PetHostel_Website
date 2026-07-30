from django.db import models


# Create your models here.
class Contact(models.Model):
    location = models.TextField(max_length=50)
    phone_number = models.TextField(max_length=18)
    email = models.EmailField()

    def __str__(self):
        return self.location


class CustomerContact(models.Model):
    name = models.TextField(max_length=30)
    contact_email = models.EmailField()
    pet_type = models.Choices("Dog", "cat")
    message = models.TextField(max_length=200)

    def __str__(self):
        return self.name
