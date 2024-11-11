from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


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


@receiver(post_save, sender=Companion)
def decrease_seats_available(sender, instance, created, **kwargs):
    if created:
        # ijasha az ChatGPT giriftam. guzashtem yo naguzashtem dar yodam nest. seats_available yakta yakta kam shavad boyad har yak hamsafar doxil shavad.
        # online Theater ba ham seats_available doxil karda budam lekin kor karda natonista budam.
        trip = instance.trip
        if trip.seats_available > 0:
            trip.seats_available -= 1
            trip.save()



