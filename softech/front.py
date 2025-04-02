from django.urls import path

from apps.items.views import get_category

front_urlpatterns = [
    path("", get_category, name=""),
]