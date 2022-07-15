from django.contrib import admin
from django.urls import path

from config.api import history, home, btc_usd

urlpatterns = [
    path('admin/', admin.site.urls),
    path("home/", home),
    path("btc_usd/", btc_usd),
    path("history/", history)
]
