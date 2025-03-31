from django.shortcuts import render

from items.models import Category, Item


def get_category(request):
    categories = Category.objects.all()
    items = Item.objects.filter(is_available=True)
    context = {
        "categories": categories,
        "items": items
    }
    return render(request, context=context, template_name="base.html")

