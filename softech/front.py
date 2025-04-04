from django.urls import path

from apps.items.views import get_category, get_category_en

front_urlpatterns = [
    path("ru", get_category, name="ru"),
    path("en", get_category_en, name="en")
]