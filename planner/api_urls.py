from django.urls import path
from . import views
from .views import city_list, activity_list, generate_trip_plan

urlpatterns = [
    path('cities/', city_list, name='city_list'),
    path('activities/', activity_list, name='activity_list'),
    path('plan/', generate_trip_plan, name='generate_trip_plan'),
]
