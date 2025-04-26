from django import forms
from .models import City

TRAVEL_PREFERENCES = [
    ('Kültür', 'Kültür'),
    ('Gezi', 'Gezi'),
    ('Manzara', 'Manzara'),
    ('Lezzet', 'Lezzet'),
    ('Aile', 'Aile'),
]

class TripPlanForm(forms.Form):
    city = forms.ModelChoiceField(queryset=City.objects.all(), label="Şehir Seçin")
    day_count = forms.IntegerField(min_value=1, label="Kaç Günlük Seyahat?")
    budget = forms.DecimalField(min_value=0, decimal_places=2, label="Bütçeniz (₺)")
    travel_preference = forms.ChoiceField(choices=TRAVEL_PREFERENCES, label="Seyahat Tercihiniz")
