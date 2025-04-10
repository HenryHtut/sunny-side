from django.urls import path
from . import views
from .views import country_detail_view

urlpatterns = [
    path("", views.unipage, name="unipage"),
    path("landing", views.land, name="landing"),
    path("country/<int:country_id>/", country_detail_view, name="country_detail"),
]