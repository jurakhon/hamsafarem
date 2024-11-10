from django.urls import path
from .views import *

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('triplist/', TripListView.as_view(), name='trip_list'),
    path('tripdetail/<int:pk>/', TripDetailView.as_view(), name='trip_detail'),
    path('tripcreate/', TripCreateView.as_view(), name='trip_create'),
    path('tripupdate/<int:pk>/', TripUpdateView.as_view(), name='trip_update'),
    path('tripdelete/<int:pk>/', TripDeleteView.as_view(), name='trip_delete'),
    path('companionlist/', CompanionListView.as_view(), name='companion_list'),
    path('companiondetail/<int:pk>/', CompanionDetailView.as_view(), name='companion_detail'),
    path('companioncreate/', CompanionCreateView.as_view(), name='companion_create'),
    path('companionupdate/<int:pk>/', CompanionUpdateView.as_view(), name='companion_update'),
    path('companiondelete/<int:pk>/', CompanionDeleteView.as_view(), name='companion_delete'),

]