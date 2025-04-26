from django.shortcuts import render
from .forms import TripPlanForm
from .models import Activity
import random

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import CitySerializer, ActivitySerializer
from .models import City, Activity

@api_view(['GET'])
def city_list(request):
    cities = City.objects.all()
    serializer = CitySerializer(cities, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def activity_list(request):
    activities = Activity.objects.all()
    serializer = ActivitySerializer(activities, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def generate_trip_plan(request):
    city_id = request.data.get('city_id')
    day_count = request.data.get('day_count')
    budget = request.data.get('budget')
    travel_preference = request.data.get('travel_preference')

    # Gerekli alanlar kontrol
    if not all([city_id, day_count, budget, travel_preference]):
        return Response(
            {"error": "city_id, day_count, budget ve travel_preference zorunludur."},
            status=400
        )

    # Tip dönüşümleri
    try:
        city_id = int(city_id)
        day_count = int(day_count)
        budget = float(budget)
    except ValueError:
        return Response(
            {"error": "city_id ve day_count sayı olmalı, budget ise ondalıklı sayı olmalı."},
            status=400
        )

    # Şehir kontrol
    try:
        city = City.objects.get(id=city_id)
    except City.DoesNotExist:
        return Response({"error": "Şehir bulunamadı."}, status=404)

    activities = Activity.objects.filter(city=city)

    plan = create_trip_plan(activities, day_count, budget, travel_preference)

    # JSON formatında düzenleme
    serialized_plan = {}

    for day, activities_in_day in plan.items():
        serialized_plan[day] = [
            {
                "isim": activity.isim,
                "sure": activity.sure,
                "fiyat": float(activity.fiyat),
                "kategori": activity.kategori
            }
            for activity in activities_in_day
        ]

    return Response(serialized_plan)







def create_trip_plan(activities, day_count, budget, travel_preference):
    plan = {}
    activities = list(activities)

    # Skorlama: Tercihe uygun aktiviteleri ön plana al
    scored_activities = []

    for activity in activities:
        score = 0
        if activity.kategori == travel_preference:
            score += 10  # Tercih edilen kategoriye uyuyorsa ekstra puan
        scored_activities.append((activity, score))

    # Skora göre sırala (yüksek puanlılar başa)
    scored_activities.sort(key=lambda x: x[1], reverse=True)

    remaining_budget = float(budget)

    for day in range(1, day_count + 1):
        daily_plan = []
        daily_time = 0

        for activity, score in scored_activities:
            if activity.fiyat <= remaining_budget and daily_time + activity.sure <= 8:
                if activity not in daily_plan:  # Aynı aktiviteyi iki kere eklememek için
                    daily_plan.append(activity)
                    remaining_budget -= float(activity.fiyat)
                    daily_time += activity.sure

        plan[f"Gün {day}"] = daily_plan

    return plan


def trip_planner(request):
    plan = None

    if request.method == "POST":
        form = TripPlanForm(request.POST)
        if form.is_valid():
            city = form.cleaned_data["city"]
            day_count = form.cleaned_data["day_count"]
            budget = form.cleaned_data["budget"]
            travel_preference = form.cleaned_data["travel_preference"]

            activities = Activity.objects.filter(city=city)

            # Skora göre plan oluştur
            plan = create_trip_plan(activities, day_count, budget, travel_preference)

    else:
        form = TripPlanForm()

    return render(request, "planner/trip_planner.html", {"form": form, "plan": plan})



