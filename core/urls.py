from django.urls import path

from . import views

urlpatterns = [
    path("stations/", views.stations_list, name="stations-list"),
]