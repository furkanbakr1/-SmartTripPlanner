
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('planner.urls')),
    path('api/', include('planner.api_urls'))
]
