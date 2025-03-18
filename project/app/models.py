from django.db import models

class Customer(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.PositiveBigIntegerField()
    password = models.CharField(max_length=255)
    location = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Staf(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)
    location = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class AdminReg(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.PositiveBigIntegerField()
    password = models.CharField(max_length=255)

    def __str__(self):
        return self.name
    
class TourPackage(models.Model):
    name = models.CharField(max_length=255)
    destination = models.CharField(max_length=255)
    duration = models.IntegerField(help_text="Duration in days")
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()
    availability = models.IntegerField(help_text="Number of slots available")

    def __str__(self):
        return self.name

class Transport(models.Model):
    TRANSPORT_TYPES = [
        ('Flight', 'Flight'),
        ('Bus', 'Bus'),
        ('Train', 'Train'),
        ('Private Car', 'Private Car'),
    ] 
    mode = models.CharField(max_length=50, choices=TRANSPORT_TYPES)
    provider = models.CharField(max_length=255)
    departure = models.DateTimeField()
    arrival = models.DateTimeField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    availability = models.IntegerField()

    def __str__(self):
        return f"{self.mode} - {self.provider}"

class Hotel(models.Model):
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    rating = models.FloatField()
    price_per_night = models.DecimalField(max_digits=10, decimal_places=2)
    available_rooms = models.IntegerField()

    def __str__(self):
        return self.name
