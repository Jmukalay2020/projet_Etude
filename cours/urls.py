from django.urls import path
from .views import acceuilView
from .views import aboutView

urlpatterns = [
    path('', acceuilView, name="acceuil"),
    path('about', aboutView, name="apropos"),
]