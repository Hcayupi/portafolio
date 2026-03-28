from django.urls import path
from .views import index,portafolio_view


urlpatterns = [
    path("", index, name="index"),
    path("/portafolio", portafolio_view, name="portafolio")
]
