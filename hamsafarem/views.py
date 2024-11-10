from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.http import HttpResponse
from django.urls import reverse, reverse_lazy
from django.views import View
from django.views.generic import ListView, TemplateView, DetailView, CreateView, UpdateView, DeleteView
from .models import *
#from .forms import *

# Create your views here.

class HomeView(TemplateView):
    template_name = "home.html"
    context_object_name = "home"


class TripListView(ListView):
    model = Trip
    context_object_name = "trip_list"
    template_name = "trip_list.html"

class TripDetailView(DetailView):
    model = Trip
    context_object_name = "trip_detail"
    template_name = "trip_detail.html"

class TripCreateView(CreateView):
    model = Trip
    fields = ['user', 'title', 'start_location', 'end_location', 'date', 'seats_available', 'description']
    template_name = "trip_create.html"
    success_url = reverse_lazy("trip_list")

class TripUpdateView(UpdateView):
    model = Trip
    fields = ['user', 'title', 'start_location', 'end_location', 'date', 'seats_available', 'description']
    template_name = "trip_update.html"
    success_url = reverse_lazy("trip_list")

class TripDeleteView(DeleteView):
    model = Trip
    template_name = "confirm_trip_delete.html"
    success_url = reverse_lazy("trip_list")

class CompanionListView(ListView):
    model = Companion
    context_object_name = "companion_list"
    template_name = "companion_list.html"

class CompanionDetailView(DetailView):
    model = Companion
    context_object_name = "companion_detail"
    template_name = "companion_detail.html"

class CompanionCreateView(CreateView):
    model = Companion
    fields = ['user', 'trip', 'description']
    template_name = "companion_create.html"
    success_url = reverse_lazy("companion_list")

class CompanionUpdateView(UpdateView):
    model = Companion
    fields = ['user', 'trip', 'description']
    template_name = "companion_update.html"
    success_url = reverse_lazy("companion_list")

class CompanionDeleteView(DeleteView):
    model = Companion
    template_name = "confirm_companion_delete.html"
    success_url = reverse_lazy("companion_list")
