# SmartTripPlanner

SmartTripPlanner, kullanıcıların seçtikleri şehre, gün sayısına ve bütçelerine göre seyahat planı oluşturan bir Django tabanlı uygulamadır.

## Özellikler

- Şehir ve aktivite veritabanı yönetimi
- Kullanıcıdan şehir, gün, bütçe ve seyahat tercihi alma
- AI destekli (basit puanlama) seyahat planı oluşturma
- JSON API desteği (Django REST Framework)
- Responsive frontend (Bootstrap kullanılarak)
- Postman ile API testleri

## Kurulum

1. Depoyu klonlayın:
    ```bash
    git clone https://github.com/furkanbakr1/SmartTripPlanner.git
    cd SmartTripPlanner
    ```

2. Ortamı hazırlayın:
    ```bash
    python -m venv env
    env\Scripts\activate
    pip install -r requirements.txt
    ```

3. Veritabanını hazırlayın:
    ```bash
    python manage.py migrate
    ```

4. Sunucuyu başlatın:
    ```bash
    python manage.py runserver
    ```

5. Admin paneline erişin:
    ```
    http://127.0.0.1:8000/admin
    ```

## 📬 API Kullanımı

- `POST /api/plan/` → Şehir, gün sayısı, bütçe ve tercih göndererek seyahat planı alınır.

İstek Örneği:

```json
{
    "city_id": 1,
    "day_count": 3,
    "budget": 1000,
    "travel_preference": "Kültür"
}
