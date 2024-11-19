from django.db import models
from django.forms import ValidationError
from django.utils import timezone

class Menu(models.Model):
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    inventory = models.PositiveIntegerField()
    
    def get_item(self):
        return f"{self.title}: {self.price}"
    
    def __str__(self):
        return self.title
    
class Booking(models.Model):
    name = models.CharField(max_length=255)
    no_of_guests = models.IntegerField()
    bookingDate = models.DateTimeField()
    
    def clean(self):
        local_now = timezone.localtime(timezone.now())
        if self.bookingDate < local_now:
            raise ValidationError("The booking date cannot be in the past.")
        
        if self.no_of_guests < 1:
            raise ValidationError("The number of people must be greater than zero.")
    
    def save(self, *args, **kwargs):
        self.clean()  # Calls the validation
        super().save(*args, **kwargs)
        
    def __str__(self):
        return self.name