from django.db import models
from datetime import datetime
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.
class Booking(models.Model):
    booking_ID = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    no_of_guests = models.IntegerField(validators=[MinValueValidator(0),MaxValueValidator(6)])
    booking_date = models.DateTimeField(default=datetime.now)
    
class Menu(models.Model):
    menu_ID = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=255)
    price = models.DecimalField(decimal_places=2, max_digits=10)
    inventory = models.IntegerField(validators=[MinValueValidator(0),MaxValueValidator(5)])