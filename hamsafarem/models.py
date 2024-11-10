from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Trip(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    start_location = models.CharField(max_length=50)
    end_location = models.CharField(max_length=50)
    date = models.DateField()
    seats_available = models.IntegerField()
    description = models.TextField()
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.start_location} - {self.end_location} - {self.date}"

class Companion(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    trip = models.ForeignKey(Trip, on_delete=models.CASCADE)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return f"{self.user.username} - {self.trip.start_location} - {self.trip.end_location}"





