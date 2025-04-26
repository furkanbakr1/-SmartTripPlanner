from django.db import models

class City(models.Model):
    isim = models.CharField(max_length=100)
    ulke = models.CharField(max_length=100)

    def __str__(self):
        return self.isim


class Activity(models.Model):
    city = models.ForeignKey(City, on_delete=models.CASCADE, related_name='aktiviteler')
    isim = models.CharField(max_length=200)
    fiyat = models.DecimalField(max_digits=10, decimal_places=2)
    sure = models.FloatField(help_text="Etkinlik süresi saat cinsinden")
    kategori = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.isim} ({self.city.isim})"
