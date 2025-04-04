from django.shortcuts import render
from apps.items.services import TemplateService


def get_category(request):
    data = TemplateService()
    categories = data.get_category()

    sub_categories = {}
    for category in categories:
        sub_categories[category.id] = data.get_subcategory(category.id)

    items = data.get_items()

    context = {
        "categories": categories,
        "sub_categories": sub_categories,
        "items": items,
    }

    return render(request, context=context, template_name="base.html")



def get_category_en(request):
    data = TemplateService()
    categories = data.get_category()

    sub_categories = {}
    for category in categories:
        sub_categories[category.id] = data.get_subcategory(category.id)

    items = data.get_items()

    context = {
        "categories": categories,
        "sub_categories": sub_categories,
        "items": items,
    }

    return render(request, context=context, template_name="base_en.html")
