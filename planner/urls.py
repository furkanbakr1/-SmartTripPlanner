from django.urls import path
from . import views

urlpatterns = [
    path('plan/', views.trip_planner, name="trip_planner"),
]
