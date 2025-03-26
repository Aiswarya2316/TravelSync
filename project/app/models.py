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
    
from django.db import models

class TourPackage(models.Model):
    name = models.CharField(max_length=255)
    destination = models.CharField(max_length=255)
    duration = models.IntegerField(help_text="Duration in days")
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()
    availability = models.IntegerField(help_text="Number of slots available")
    image = models.ImageField(upload_to='tour_packages/', null=True, blank=True)

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
    image = models.ImageField(upload_to='transport/', null=True, blank=True)

    def __str__(self):
        return f"{self.mode} - {self.provider}"

class Hotel(models.Model):
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    rating = models.FloatField()
    price_per_night = models.DecimalField(max_digits=10, decimal_places=2)
    available_rooms = models.IntegerField()
    image = models.ImageField(upload_to='hotels/', null=True, blank=True)

    def __str__(self):
        return self.name


class Booking(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    tour_package = models.ForeignKey(TourPackage, on_delete=models.SET_NULL, null=True, blank=True)
    hotel = models.ForeignKey(Hotel, on_delete=models.SET_NULL, null=True, blank=True)
    transport = models.ForeignKey(Transport, on_delete=models.SET_NULL, null=True, blank=True)
    status = models.CharField(max_length=20, choices=[("Confirmed", "Confirmed"), ("Pending", "Pending"), ("Cancelled", "Cancelled")], default="Pending")
    booking_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        if self.tour_package:
            return f"Package: {self.tour_package.name} - {self.customer}"
        elif self.hotel:
            return f"Hotel: {self.hotel.name} - {self.customer}"
        elif self.transport:
            return f"Transport: {self.transport.TRANSPORT_TYPES} - {self.customer}"
        return f"Booking - {self.customer}"

