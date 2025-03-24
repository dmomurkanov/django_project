from django.shortcuts import render

from items.models import Category


def get_category(request):
    categories = Category.objects.all()
    context = {
        "categories": categories
    }
    return render(request, context=context, template_name="base.html")