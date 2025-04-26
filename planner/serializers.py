from rest_framework import serializers
from .models import City, Activity

class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = ['id', 'isim', 'ulke']

class ActivitySerializer(serializers.ModelSerializer):
    city = CitySerializer()  # Şehrin bilgilerini de gösterir

    class Meta:
        model = Activity
        fields = ['id', 'city', 'isim', 'fiyat', 'sure', 'kategori']
