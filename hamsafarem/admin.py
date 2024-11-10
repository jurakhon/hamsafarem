from django.contrib import admin
from hamsafarem.models import Trip, Companion
# Register your models here.

@admin.register(Trip)
class TripAdmin(admin.ModelAdmin):
    list_display = ['user', 'start_location', 'end_location','date','seats_available']
    list_filter = ['date', 'seats_available']
    search_fields = ['user', 'date', 'seats_available', 'start_location','end_location']



@admin.register(Companion)
class CompanionAdmin(admin.ModelAdmin):
    list_display = ['user', 'trip']
    list_filter = ['user','created_at']
    search_fields = ['user', 'created_at', 'description']
